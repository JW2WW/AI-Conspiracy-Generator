import pytest


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
