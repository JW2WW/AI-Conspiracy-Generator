import json
from pathlib import Path

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# Resolve the .env location independently of the current working directory so
# the backend loads the same file whether it is started from the repo root or
# from the backend/ directory. A backend-local .env takes precedence over the
# repo-root .env (used by docker compose).
_BACKEND_DIR = Path(__file__).resolve().parents[1]
_ENV_FILES = (_BACKEND_DIR.parent / ".env", _BACKEND_DIR / ".env")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=_ENV_FILES,
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "AI Conspiracy Generator"
    debug: bool = False

    database_url: str = "postgresql+asyncpg://conspiracy:conspiracy@postgres:5432/conspiracy"
    redis_url: str = "redis://redis:6379/0"

    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    openrouter_api_key: str | None = None
    llm_provider: str = "mock"
    openai_model: str = "gpt-4o-mini"
    anthropic_model: str = "claude-3-5-haiku-20241022"
    openrouter_model: str = "openrouter/free"
    openrouter_base_url: str = "https://openrouter.ai/api/v1"
    openrouter_site_url: str = "https://github.com/JW2WW/AI-Conspiracy-Generator"
    openrouter_app_name: str = "AI Conspiracy Generator"

    cors_origins: list[str] = ["http://localhost:5173", "http://localhost:3000"]

    @field_validator("cors_origins", mode="before")
    @classmethod
    def parse_cors_origins(cls, value: str | list[str]) -> list[str]:
        if isinstance(value, str):
            try:
                return json.loads(value)
            except json.JSONDecodeError:
                return [origin.strip() for origin in value.split(",")]
        return value


settings = Settings()
