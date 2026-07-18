import json
import random
import re
from abc import ABC, abstractmethod
from typing import ClassVar

from anthropic import AsyncAnthropic
from openai import AsyncOpenAI

from app.config import settings


class LLMProvider(ABC):
    @abstractmethod
    async def generate(self, system_prompt: str, user_prompt: str) -> str:
        pass


class OpenAIProvider(LLMProvider):
    def __init__(self) -> None:
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def generate(self, system_prompt: str, user_prompt: str) -> str:
        response = await self.client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.9,
            max_tokens=800,
        )
        return response.choices[0].message.content or ""


class AnthropicProvider(LLMProvider):
    def __init__(self) -> None:
        self.client = AsyncAnthropic(api_key=settings.anthropic_api_key)

    async def generate(self, system_prompt: str, user_prompt: str) -> str:
        response = await self.client.messages.create(
            model=settings.anthropic_model,
            max_tokens=800,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
            temperature=0.9,
        )
        return response.content[0].text if response.content else ""


class MockProvider(LLMProvider):
    """Template-based responses for demo mode without API keys."""

    CORPORATIONS: ClassVar[list[str]] = [
        "Global Acorn Dynamics Corporation",
        "OmniSquirrel Industries",
        "Nexus Timeline Holdings",
        "PaleoTech Megacorp",
    ]

    async def generate(self, system_prompt: str, user_prompt: str) -> str:
        role = self._detect_role(system_prompt)
        event = self._extract_event(user_prompt)
        mode = self._extract_mode(system_prompt)
        round_num = self._extract_round(user_prompt)

        generators = {
            "theory": self._theory,
            "investigator": self._investigator,
            "judge": self._judge,
            "evidence": self._evidence,
            "reality": self._reality,
        }
        return generators[role](event, mode, round_num)

    def _detect_role(self, system_prompt: str) -> str:
        prompt = system_prompt.lower()
        if "judge" in prompt or "score" in prompt:
            return "judge"
        if "investigator" in prompt or "debunk" in prompt or "fact-check" in prompt:
            return "investigator"
        if "evidence" in prompt or "timeline" in prompt:
            return "evidence"
        if "reality" in prompt or "actual cause" in prompt:
            return "reality"
        return "theory"

    def _extract_event(self, user_prompt: str) -> str:
        match = re.search(r"Event:\s*(.+?)(?:\n|$)", user_prompt, re.IGNORECASE)
        if match:
            return match.group(1).strip()
        lines = [line.strip() for line in user_prompt.splitlines() if line.strip()]
        return lines[-1] if lines else "the mysterious event"

    def _extract_mode(self, system_prompt: str) -> str:
        for mode in ("xfiles", "corporate", "time_traveler", "ancient", "escalation", "debate", "classic"):
            if mode in system_prompt.lower():
                return mode
        return "classic"

    def _extract_round(self, user_prompt: str) -> int:
        match = re.search(r"round\s*(\d+)", user_prompt, re.IGNORECASE)
        return int(match.group(1)) if match else 1

    def _theory(self, event: str, mode: str, round_num: int) -> str:
        corp = random.choice(self.CORPORATIONS)
        if round_num == 1:
            debate_villain = "squirrel operatives"
        elif round_num == 2:
            debate_villain = "a global shadow network"
        else:
            debate_villain = "interdimensional puppet masters"
        theories = {
            "classic": [
                f"The event ({event}) coincided with three missing cats and a delivery truck from an unknown company. "
                "This strongly suggests an underground squirrel organization is testing "
                "electromagnetic acorn technology.",
                f"Regarding '{event}': local pigeons have been observed wearing tiny reflective bands. "
                "Clearly a coordinated surveillance network is monitoring civilian activity.",
            ],
            "xfiles": [
                f"'{event}' was not random. A black helicopter was spotted 47 minutes prior. "
                "Area 51-adjacent contractors are testing reverse-engineered alien power dampeners.",
                f"The event ({event}) aligns with classified Project MOONSHADOW activity. "
                "Government agents replaced standard equipment with paranormal resonance suppressors.",
            ],
            "corporate": [
                f"The event ({event}) was orchestrated by {corp} to beta-test next-generation "
                "squirrel communication infrastructure disguised as routine maintenance.",
                f"{corp} deployed covert field agents to simulate '{event}' while harvesting "
                "behavioral data from affected residents.",
            ],
            "time_traveler": [
                f"'{event}' is a temporal ripple from Timeline B-7, where a time traveler "
                "accidentally left a chronometer near critical infrastructure in 1987.",
                f"A paradox correction event caused '{event}'. Future historians will mark this "
                "as the moment the multiverse briefly sneezed.",
            ],
            "ancient": [
                f"'{event}' activated a dormant Atlantean harmonic resonator buried beneath the area. "
                "Ancient builders encoded warnings in petroglyphs that modern engineers ignored.",
                f"Lemurian crystal networks beneath the surface responded to '{event}' — "
                "a sign the old civilization's warning systems still function.",
            ],
            "escalation": [
                f"Round {round_num}: Squirrels caused the event related to '{event}'.",
                f"Round {round_num}: The squirrels are organized and report to a shadow council.",
                f"Round {round_num}: The squirrels answer to an interdimensional acorn council "
                f"governing all nut-based civilizations across seven realities.",
                f"Round {round_num}: '{event}' was the opening move in the Acorn Singularity — "
                "when all timelines converge into one giant hazelnut.",
            ],
            "debate": [
                f"Round {round_num} theory: '{event}' proves a coordinated conspiracy involving " f"{debate_villain}.",
            ],
        }
        options = theories.get(mode, theories["classic"])
        idx = min(round_num - 1, len(options) - 1)
        return options[idx]

    def _investigator(self, event: str, _mode: str, round_num: int) -> str:
        causes = [
            "a contractor accidentally struck a transformer with a backhoe",
            "routine maintenance on aging infrastructure",
            "a weather-related equipment failure",
            "a software update that triggered an automatic safety shutdown",
            "human error during a scheduled inspection",
        ]
        cause = random.choice(causes)
        return (
            f"Investigation into '{event}' (Round {round_num}):\n\n"
            f"Utility records and eyewitness accounts indicate the most likely cause was {cause}. "
            "No evidence of squirrel technology, alien interference, corporate sabotage, "
            "time travel paradoxes, or ancient civilizations was discovered. "
            "Correlation with unrelated events does not establish causation."
        )

    def _evidence(self, event: str, _mode: str, _round_num: int) -> str:
        return (
            f"Evidence summary for '{event}':\n\n"
            "- Timestamp: Event occurred during standard business hours\n"
            "- Witnesses: 3 independent accounts, no consensus on supernatural causes\n"
            "- Physical evidence: Standard equipment wear, no anomalous materials\n"
            "- Timeline: No gaps suggesting covert operations\n"
            "- Contradictions in conspiracy narrative: Multiple mutually exclusive explanations proposed"
        )

    def _judge(self, event: str, _mode: str, _round_num: int) -> str:
        creativity = random.randint(7, 10)
        plausibility = random.randint(0, 2)
        evidence_score = random.randint(0, 2)
        comedy = random.randint(7, 10)
        return json.dumps(
            {
                "creativity": creativity,
                "plausibility": plausibility,
                "evidence": evidence_score,
                "comedy": comedy,
                "commentary": (
                    f"A masterclass in narrative construction around '{event}'. "
                    "Creatively brilliant, empirically bankrupt — exactly as intended."
                ),
            }
        )

    def _reality(self, event: str, _mode: str, _round_num: int) -> str:
        return (
            f"Actual Cause\n\n"
            f"After reviewing all available evidence regarding '{event}', "
            "the most likely explanation is mundane equipment failure or human error "
            "during routine operations. No conspiracy was found.\n\n"
            "Case Closed."
        )


def get_llm_provider() -> LLMProvider:
    provider = settings.llm_provider.lower()
    if provider == "openai" and settings.openai_api_key:
        return OpenAIProvider()
    if provider == "anthropic" and settings.anthropic_api_key:
        return AnthropicProvider()
    return MockProvider()


def parse_judge_scores(text: str) -> dict:
    try:
        match = re.search(r"\{[^{}]*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except json.JSONDecodeError:
        pass

    scores = {"creativity": 8, "plausibility": 1, "evidence": 1, "comedy": 9, "commentary": text[:200]}
    for key in ("creativity", "plausibility", "evidence", "comedy"):
        match = re.search(rf"{key}:\s*(\d+)", text, re.IGNORECASE)
        if match:
            scores[key] = int(match.group(1))
    return scores
