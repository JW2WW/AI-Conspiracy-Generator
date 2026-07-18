import asyncio
import hashlib
import json
import uuid
from datetime import UTC, datetime

import redis.asyncio as redis

from app.agents import (
    EvidenceAgent,
    InvestigatorAgent,
    JudgeAgent,
    RealityRestoredEngine,
    TheoryAgent,
)
from app.config import settings
from app.models.schemas import ConspiracyRequest, ConspiracyResponse, DebateRound, ScoreBreakdown
from app.services.llm import get_llm_provider
from app.services.sanitizer import sanitize_event


class ConspiracyOrchestrator:
    _TIMEOUT_SECONDS = 120

    def __init__(self) -> None:
        llm = get_llm_provider()
        self.theory_agent = TheoryAgent(llm)
        self.investigator_agent = InvestigatorAgent(llm)
        self.evidence_agent = EvidenceAgent(llm)
        self.judge_agent = JudgeAgent(llm)
        self.reality_engine = RealityRestoredEngine(llm)
        self._redis: redis.Redis | None = None

    async def _get_redis(self) -> redis.Redis:
        if self._redis is None:
            self._redis = redis.from_url(settings.redis_url, decode_responses=True)
        return self._redis

    def _rounds_for_mode(self, request: ConspiracyRequest) -> int:
        return max(request.rounds, 1)

    async def generate(self, request: ConspiracyRequest) -> ConspiracyResponse:
        try:
            return await asyncio.wait_for(self._generate_inner(request), timeout=self._TIMEOUT_SECONDS)
        except TimeoutError:
            raise RuntimeError("Generation timed out. Try a simpler event or fewer rounds.") from None

    async def _generate_inner(self, request: ConspiracyRequest) -> ConspiracyResponse:
        safe_event = sanitize_event(request.event)
        event_hash = hashlib.md5(safe_event.encode()).hexdigest()
        cache_key = f"conspiracy:{request.game_mode.value}:{event_hash}:{request.rounds}"
        r = await self._get_redis()
        cached = await r.get(cache_key)
        if cached:
            data = json.loads(cached)
            return ConspiracyResponse(**data)

        num_rounds = self._rounds_for_mode(request)
        evidence = await self.evidence_agent.gather(safe_event)

        debate_rounds: list[DebateRound] = []
        all_theories: list[str] = []
        all_investigations: list[str] = []
        context = f"Evidence gathered:\n{evidence}"

        final_theory = ""
        final_investigation = ""

        for round_num in range(1, num_rounds + 1):
            theory = await self.theory_agent.generate(safe_event, request.game_mode, round_num, context)
            investigation = await self.investigator_agent.investigate(safe_event, theory, round_num)

            debate_rounds.append(DebateRound(round_number=round_num, theory=theory, investigation=investigation))
            all_theories.append(theory)
            all_investigations.append(investigation)
            final_theory = theory
            final_investigation = investigation
            context += f"\n\nRound {round_num} Theory: {theory}\nRound {round_num} Investigation: {investigation}"

        scores_raw = await self.judge_agent.score(safe_event, final_theory, final_investigation)
        scores = ScoreBreakdown(**scores_raw)

        reality = await self.reality_engine.reveal(safe_event, all_theories, all_investigations)

        response = ConspiracyResponse(
            id=str(uuid.uuid4()),
            event=request.event,
            game_mode=request.game_mode,
            evidence=evidence,
            theory=final_theory,
            investigation=final_investigation,
            debate_rounds=debate_rounds,
            scores=scores,
            reality_restored=reality,
            created_at=datetime.now(UTC),
            metadata={"llm_provider": settings.llm_provider, "rounds": num_rounds},
        )

        await r.setex(cache_key, 3600, response.model_dump_json())
        return response

    async def close(self) -> None:
        if self._redis:
            await self._redis.aclose()


orchestrator = ConspiracyOrchestrator()
