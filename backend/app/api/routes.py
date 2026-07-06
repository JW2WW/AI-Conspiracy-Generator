from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.config import settings
from app.models import (
    ConspiracyRequest,
    ConspiracyResponse,
    ConspiracySession,
    GameMode,
    GameModeInfo,
    HealthResponse,
    get_db,
)
from app.services.orchestrator import orchestrator

router = APIRouter()

GAME_MODES = [
    GameModeInfo(
        id=GameMode.CLASSIC,
        name="Classic Conspiracy",
        description="Create increasingly elaborate conspiracy theories with escalating absurdity.",
    ),
    GameModeInfo(
        id=GameMode.XFILES,
        name="X-Files Mode",
        description="Every event involves aliens, government coverups, secret facilities, or paranormal activity.",
    ),
    GameModeInfo(
        id=GameMode.CORPORATE,
        name="Corporate Conspiracy",
        description="Blame everything on a fictional mega-corporation with sinister motives.",
    ),
    GameModeInfo(
        id=GameMode.TIME_TRAVELER,
        name="Time Traveler Mode",
        description="Explain events through timeline manipulation and paradoxes.",
    ),
    GameModeInfo(
        id=GameMode.ANCIENT,
        name="Ancient Civilization",
        description="Trace everything back to lost civilizations and ancient technology.",
    ),
    GameModeInfo(
        id=GameMode.DEBATE,
        name="AI Debate Mode",
        description="Theory and Investigator agents engage in multiple debate rounds.",
    ),
    GameModeInfo(
        id=GameMode.ESCALATION,
        name="Escalation Mode",
        description="Each round must become more absurd than the previous one.",
    ),
]


@router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="ok", llm_provider=settings.llm_provider)


@router.get("/modes", response_model=list[GameModeInfo])
async def list_modes() -> list[GameModeInfo]:
    return GAME_MODES


@router.post("/generate", response_model=ConspiracyResponse)
async def generate_conspiracy(
    request: ConspiracyRequest,
    db: AsyncSession = Depends(get_db),
) -> ConspiracyResponse:
    try:
        result = await orchestrator.generate(request)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Generation failed: {exc}") from exc

    session = ConspiracySession(
        id=result.id,
        event=request.event,
        game_mode=request.game_mode.value,
        result=result.model_dump(mode="json"),
    )
    db.add(session)
    await db.commit()

    return result


@router.get("/sessions/{session_id}", response_model=ConspiracyResponse)
async def get_session(session_id: str, db: AsyncSession = Depends(get_db)) -> ConspiracyResponse:
    from sqlalchemy import select

    result = await db.execute(select(ConspiracySession).where(ConspiracySession.id == session_id))
    session = result.scalar_one_or_none()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")
    return ConspiracyResponse(**session.result)
