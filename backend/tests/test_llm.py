"""Tests for the LLM provider layer."""

import json
import types

import pytest

from app.config import settings
from app.services.llm import (
    GeminiProvider,
    MockProvider,
    OpenRouterProvider,
    _chat_completion,
    _strip_thought_blocks,
    get_llm_provider,
    parse_judge_scores,
)


def _make_response(content: str | None = None, error: object = None):
    if content is not None:
        message = types.SimpleNamespace(content=content)
        return types.SimpleNamespace(choices=[types.SimpleNamespace(message=message)], error=None)
    return types.SimpleNamespace(choices=None, error=error)


class _FakeCompletions:
    def __init__(self, responses):
        self._responses = list(responses)
        self.calls = 0

    async def create(self, **_kwargs):
        response = self._responses[self.calls]
        self.calls += 1
        return response


class _FakeClient:
    def __init__(self, responses):
        self.chat = types.SimpleNamespace(completions=_FakeCompletions(responses))


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


def test_get_openrouter_provider(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(settings, "llm_provider", "openrouter")
    monkeypatch.setattr(settings, "openrouter_api_key", "test-key")

    provider = get_llm_provider()

    assert isinstance(provider, OpenRouterProvider)
    assert str(provider.client.base_url) == "https://openrouter.ai/api/v1/"


def test_openrouter_requires_api_key(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(settings, "llm_provider", "openrouter")
    monkeypatch.setattr(settings, "openrouter_api_key", None)

    with pytest.raises(ValueError, match="OPENROUTER_API_KEY"):
        get_llm_provider()


def test_get_gemini_provider(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(settings, "llm_provider", "gemini")
    monkeypatch.setattr(settings, "gemini_api_key", "test-key")

    provider = get_llm_provider()

    assert isinstance(provider, GeminiProvider)
    assert str(provider.client.base_url) == "https://generativelanguage.googleapis.com/v1beta/openai/"


def test_gemini_requires_api_key(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(settings, "llm_provider", "gemini")
    monkeypatch.setattr(settings, "gemini_api_key", None)

    with pytest.raises(ValueError, match="GEMINI_API_KEY"):
        get_llm_provider()


@pytest.mark.asyncio
async def test_chat_completion_returns_content():
    client = _FakeClient([_make_response(content="the truth is out there")])
    result = await _chat_completion(client, "some/model", "sys", "user")
    assert result == "the truth is out there"


@pytest.mark.asyncio
async def test_chat_completion_retries_transient_empty_response(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("app.services.llm.asyncio.sleep", _noop_sleep)
    client = _FakeClient(
        [
            _make_response(error={"message": "temporarily rate-limited"}),
            _make_response(content="recovered"),
        ]
    )
    result = await _chat_completion(client, "some/model", "sys", "user")
    assert result == "recovered"
    assert client.chat.completions.calls == 2


@pytest.mark.asyncio
async def test_chat_completion_raises_after_exhausting_retries(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("app.services.llm.asyncio.sleep", _noop_sleep)
    client = _FakeClient([_make_response(error={"message": "upstream is down"}) for _ in range(3)])
    with pytest.raises(RuntimeError, match="upstream is down"):
        await _chat_completion(client, "some/model", "sys", "user")


async def _noop_sleep(_seconds: float) -> None:
    return None


def test_strip_thought_blocks_removes_reasoning():
    text = "<thought>planning the joke</thought>\nThe squirrels did it."
    assert _strip_thought_blocks(text) == "The squirrels did it."


def test_strip_thought_blocks_keeps_raw_when_only_thought():
    text = "<thought>still thinking</thought>"
    assert _strip_thought_blocks(text) == text


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
