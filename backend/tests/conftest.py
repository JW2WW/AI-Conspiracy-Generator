import pytest


@pytest.fixture(autouse=True)
def _mock_redis(monkeypatch: pytest.MonkeyPatch) -> None:
    """Prevent tests from connecting to real Redis."""

    async def mock_get_redis(self) -> None:
        import fakeredis  # type: ignore[import-untyped]

        self._redis = await fakeredis.FakeAsyncRedis(decode_responses=True)

    monkeypatch.setattr(
        "app.services.orchestrator.ConspiracyOrchestrator._get_redis",
        mock_get_redis,
    )