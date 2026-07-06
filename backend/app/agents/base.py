from app.agents.prompts import (
    EVIDENCE_SYSTEM,
    INVESTIGATOR_SYSTEM,
    JUDGE_SYSTEM,
    MODE_INSTRUCTIONS,
    REALITY_SYSTEM,
    THEORY_SYSTEM,
)
from app.models.schemas import GameMode
from app.services.llm import LLMProvider, parse_judge_scores


class TheoryAgent:
    def __init__(self, llm: LLMProvider) -> None:
        self.llm = llm

    async def generate(self, event: str, game_mode: GameMode, round_num: int = 1, context: str = "") -> str:
        system = THEORY_SYSTEM.format(mode_instruction=MODE_INSTRUCTIONS[game_mode])
        user = f"Event: {event}\nGame mode: {game_mode.value}\nRound: {round_num}"
        if context:
            user += f"\n\nPrior context:\n{context}"
        return await self.llm.generate(system, user)


class InvestigatorAgent:
    def __init__(self, llm: LLMProvider) -> None:
        self.llm = llm

    async def investigate(self, event: str, theory: str, round_num: int = 1) -> str:
        user = f"Event: {event}\nRound: {round_num}\n\nTheory to investigate:\n{theory}"
        return await self.llm.generate(INVESTIGATOR_SYSTEM, user)


class EvidenceAgent:
    def __init__(self, llm: LLMProvider) -> None:
        self.llm = llm

    async def gather(self, event: str) -> str:
        user = f"Event: {event}\n\nGather evidence and build a factual timeline."
        return await self.llm.generate(EVIDENCE_SYSTEM, user)


class JudgeAgent:
    def __init__(self, llm: LLMProvider) -> None:
        self.llm = llm

    async def score(self, event: str, theory: str, investigation: str) -> dict:
        user = (
            f"Event: {event}\n\nTheory:\n{theory}\n\nInvestigation:\n{investigation}\n\n"
            "Score this conspiracy theory."
        )
        raw = await self.llm.generate(JUDGE_SYSTEM, user)
        return parse_judge_scores(raw)


class RealityRestoredEngine:
    def __init__(self, llm: LLMProvider) -> None:
        self.llm = llm

    async def reveal(self, event: str, theories: list[str], investigations: list[str]) -> str:
        combined_theories = "\n---\n".join(theories)
        combined_investigations = "\n---\n".join(investigations)
        user = (
            f"Event: {event}\n\nTheories debated:\n{combined_theories}\n\n"
            f"Investigations:\n{combined_investigations}\n\nReveal the actual cause."
        )
        return await self.llm.generate(REALITY_SYSTEM, user)
