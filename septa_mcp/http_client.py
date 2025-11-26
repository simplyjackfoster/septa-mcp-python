"""HTTP client utilities for interacting with SEPTA APIs."""

import logging

import httpx

from .config import Config

logger = logging.getLogger(__name__)


class HttpClient:
    """Wrapper around ``httpx.AsyncClient`` with sensible defaults."""

    def __init__(self, client: httpx.AsyncClient) -> None:
        self._client = client

    async def get(self, path: str, **kwargs) -> httpx.Response:
        """Perform a GET request using the configured base URL."""

        logger.debug("Sending GET request to %s", path)
        response = await self._client.get(path, **kwargs)
        response.raise_for_status()
        return response

    async def close(self) -> None:
        """Close the underlying HTTP client."""

        await self._client.aclose()


async def create_http_client(settings: Config | None = None) -> HttpClient:
    """Create an HTTP client configured for the SEPTA API."""

    config = settings or Config()
    headers = {}
    if config.api_key:
        headers["Authorization"] = f"Bearer {config.api_key}"

    client = httpx.AsyncClient(
        base_url=config.base_url,
        headers=headers,
        timeout=config.timeout_seconds,
    )
    return HttpClient(client)


# Alias used by tool registration helpers to emphasize the SEPTA-specific purpose.
SeptaHttpClient = HttpClient
