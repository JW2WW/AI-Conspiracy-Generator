import json

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    app_name: str = "AI Conspiracy Generator"
    debug: bool = False

    database_url: str = "postgresql+asyncpg://conspiracy:conspiracy@postgres:5432/conspiracy"
    redis_url: str = "redis://redis:6379/0"

    openai_api_key: str | None = None
    anthropic_api_key: str | None = None
    llm_provider: str = "mock"
    openai_model: str = "gpt-4o-mini"
    anthropic_model: str = "claude-3-5-haiku-20241022"

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
