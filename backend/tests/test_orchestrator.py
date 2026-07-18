"""Tests for the orchestrator."""

import pytest

from app.models.schemas import ConspiracyRequest, GameMode
from app.services.orchestrator import ConspiracyOrchestrator


@pytest.mark.asyncio
async def test_orchestrator_generates_classic_mode():
    """Test that the orchestrator produces a full response in classic mode."""
    orch = ConspiracyOrchestrator()
    request = ConspiracyRequest(
        event="Why did the neighborhood power go out?",
        game_mode=GameMode.CLASSIC,
        rounds=1,
    )
    result = await orch.generate(request)
    assert result.id
    assert result.event == request.event
    assert result.game_mode == GameMode.CLASSIC
    assert result.theory
    assert result.investigation
    assert result.evidence
    assert result.scores is not None
    assert result.reality_restored
    assert len(result.debate_rounds) == 1
    await orch.close()


@pytest.mark.asyncio
async def test_orchestrator_generates_debate_mode():
    """Test that debate mode generates multiple rounds."""
    orch = ConspiracyOrchestrator()
    request = ConspiracyRequest(
        event="Why is my internet slow?",
        game_mode=GameMode.DEBATE,
        rounds=2,
    )
    result = await orch.generate(request)
    assert len(result.debate_rounds) == 2
    for r in result.debate_rounds:
        assert r.theory
        assert r.investigation
    await orch.close()
