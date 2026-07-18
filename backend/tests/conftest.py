import pytest


@pytest.fixture(autouse=True)
def _force_mock_provider(monkeypatch: pytest.MonkeyPatch) -> None:
    """Keep tests hermetic: never hit a real LLM even if a .env selects one."""
    from app.config import settings

    monkeypatch.setattr(settings, "llm_provider", "mock")
    monkeypatch.setattr(settings, "openai_api_key", None)
    monkeypatch.setattr(settings, "anthropic_api_key", None)
    monkeypatch.setattr(settings, "openrouter_api_key", None)
    monkeypatch.setattr(settings, "gemini_api_key", None)


@pytest.fixture(autouse=True)
def _mock_redis(monkeypatch: pytest.MonkeyPatch) -> None:
    """Prevent tests from connecting to real Redis."""

    async def mock_get_redis(self):
        import fakeredis  # type: ignore[import-untyped]

        if self._redis is None:
            self._redis = fakeredis.FakeAsyncRedis(decode_responses=True)
        return self._redis

    monkeypatch.setattr(
        "app.services.orchestrator.ConspiracyOrchestrator._get_redis",
        mock_get_redis,
    )
