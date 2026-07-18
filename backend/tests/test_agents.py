"""Tests for the agent base classes."""

import pytest

from app.agents.base import EvidenceAgent, InvestigatorAgent, TheoryAgent
from app.models.schemas import GameMode
from app.services.llm import MockProvider


@pytest.mark.asyncio
async def test_theory_agent_generates():
    llm = MockProvider()
    agent = TheoryAgent(llm)
    result = await agent.generate("Why did the power go out?", GameMode.CLASSIC, 1)
    assert len(result) > 0


@pytest.mark.asyncio
async def test_investigator_agent_investigates():
    llm = MockProvider()
    agent = InvestigatorAgent(llm)
    result = await agent.investigate(
        "Why did the power go out?",
        "Squirrels caused it using electromagnetic acorns.",
        1,
    )
    assert len(result) > 0
    assert "Investigation" in result or "cause" in result.lower()


@pytest.mark.asyncio
async def test_evidence_agent_gathers():
    llm = MockProvider()
    agent = EvidenceAgent(llm)
    result = await agent.gather("Why did the power go out?")
    assert len(result) > 0
    assert "evidence" in result.lower() or "summary" in result.lower()
