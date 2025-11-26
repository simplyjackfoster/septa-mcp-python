"""Application configuration handling."""

from functools import lru_cache

from pydantic import BaseSettings, Field


class Config(BaseSettings):
    """Runtime configuration for the MCP server."""

    base_url: str = Field(
        "https://www3.septa.org/",
        description="Base URL for SEPTA API requests.",
    )
    timeout_seconds: float = Field(
        10.0,
        description="Default timeout for HTTP requests.",
        gt=0,
    )
    log_level: str = Field(
        "INFO",
        description="Logging level for the server.",
    )
    api_key: str | None = Field(
        default=None,
        description="Optional API key for authenticated requests.",
    )

    class Config:
        env_prefix = "SEPTA_"
        case_sensitive = False


@lru_cache
def get_settings() -> Config:
    """Return a cached settings instance loaded from environment variables."""

    return Config()  # type: ignore[arg-type]
