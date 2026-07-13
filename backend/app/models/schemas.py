from datetime import datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class GameMode(str, Enum):
    CLASSIC = "classic"
    XFILES = "xfiles"
    CORPORATE = "corporate"
    TIME_TRAVELER = "time_traveler"
    ANCIENT = "ancient"
    DEBATE = "debate"
    ESCALATION = "escalation"


class DebateRound(BaseModel):
    round_number: int
    theory: str
    investigation: str


class ScoreBreakdown(BaseModel):
    creativity: int = Field(ge=0, le=10)
    plausibility: int = Field(ge=0, le=10)
    evidence: int = Field(ge=0, le=10)
    comedy: int = Field(ge=0, le=10)
    commentary: str = ""


class ConspiracyRequest(BaseModel):
    event: str = Field(..., min_length=3, max_length=500)
    game_mode: GameMode = GameMode.CLASSIC
    rounds: int = Field(default=1, ge=1, le=5)


class ConspiracyResponse(BaseModel):
    id: str
    event: str
    game_mode: GameMode
    evidence: str
    theory: str
    investigation: str
    debate_rounds: list[DebateRound] = []
    scores: ScoreBreakdown
    reality_restored: str
    created_at: datetime | None = None
    metadata: dict[str, Any] = {}


class GameModeInfo(BaseModel):
    id: GameMode
    name: str
    description: str


class HealthResponse(BaseModel):
    status: str
    llm_provider: str
