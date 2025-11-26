"""Tool for the SEPTA TransitViewAll endpoint."""

from __future__ import annotations

from ..domain import TTLCache
from .http import FastMCP, SeptaHttpClient, fetch_json


ALL_ROUTES_CACHE = TTLCache[object](ttl_seconds=10)


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the TransitViewAll tool on the server."""

    @server.tool(
        name="transit_view_all",
        description="Return vehicle locations for all bus routes via the TransitViewAll feed.",
        input_schema={
            "type": "object",
            "properties": {
                "use_cache": {
                    "type": "boolean",
                    "description": "Use a short-lived cache to reuse recently fetched data.",
                    "default": True,
                }
            },
        },
    )
    async def transit_view_all_tool(use_cache: bool = True) -> object:
        cache_key = "transit_view_all"
        if use_cache:
            cached_response = ALL_ROUTES_CACHE.get(cache_key)
            if cached_response is not None:
                return cached_response

        response = await fetch_json(client, "TransitViewAll/", params=None)

        if use_cache:
            ALL_ROUTES_CACHE.set(cache_key, response)

        return response
