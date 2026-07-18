"""Tests for the LLM provider layer."""

import json

import pytest

from app.services.llm import MockProvider, parse_judge_scores


@pytest.mark.asyncio
async def test_mock_provider_returns_theory():
    provider = MockProvider()
    result = await provider.generate(
        "You are the Theory Agent...",
        "Event: Why did the power go out?\nGame mode: classic\nRound: 1",
    )
    assert len(result) > 0
    assert "squirrel" in result or "pigeon" in result or "event" in result.lower()


@pytest.mark.asyncio
async def test_mock_provider_returns_judge_json():
    provider = MockProvider()
    result = await provider.generate(
        "You are the Judge Agent... Score the conspiracy theory...",
        "Event: Why did the power go out?\n\nTheory:\nsomething\n\nInvestigation:\nnothing",
    )
    parsed = json.loads(result)
    assert isinstance(parsed["creativity"], int)
    assert 0 <= parsed["creativity"] <= 10


def test_parse_judge_scores_valid_json():
    text = '{"creativity": 8, "plausibility": 2, "evidence": 1, "comedy": 9, "commentary": "nice"}'
    result = parse_judge_scores(text)
    assert result["creativity"] == 8
    assert result["comedy"] == 9


def test_parse_judge_scores_fallback():
    text = "creativity: 7\nplausibility: 1\nevidence: 0\ncomedy: 8"
    result = parse_judge_scores(text)
    assert result["creativity"] == 7
    assert result["plausibility"] == 1


def test_parse_judge_scores_empty_fallback():
    text = "nothing here"
    result = parse_judge_scores(text)
    assert result["creativity"] == 8
