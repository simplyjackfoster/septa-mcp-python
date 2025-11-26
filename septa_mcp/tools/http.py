"""Helper utilities shared by MCP tools."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from ..http_client import HttpClient

SeptaHttpClient = HttpClient


async def fetch_json(client: SeptaHttpClient, path: str, params: dict[str, Any] | None = None) -> Any:
    """Fetch JSON content from a SEPTA API endpoint."""

    response = await client.get(path, params=params)
    return response.json()


__all__ = ["FastMCP", "SeptaHttpClient", "fetch_json"]
