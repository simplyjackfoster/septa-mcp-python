"""Tool for the SEPTA TransitView endpoint."""

from __future__ import annotations

from ..domain import TTLCache
from ..domain.normalization import normalize_route_name
from .http import FastMCP, SeptaHttpClient, fetch_json


ROUTE_CACHE = TTLCache[object](ttl_seconds=10)


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the TransitView tool on the server."""

    @server.tool(
        name="transit_view",
        description="Return vehicle locations for a specific bus route via the TransitView endpoint.",
        input_schema={
            "type": "object",
            "properties": {
                "route": {
                    "type": "string",
                    "description": "Bus route identifier to request from TransitView.",
                },
                "normalize": {
                    "type": "boolean",
                    "description": "Normalize the route name using common aliases before querying.",
                    "default": True,
                },
                "use_cache": {
                    "type": "boolean",
                    "description": "Use a short-lived cache to avoid repeated identical requests.",
                    "default": True,
                },
            },
            "required": ["route"],
        },
    )
    async def transit_view_tool(
        route: str, normalize: bool = True, use_cache: bool = True
    ) -> object:
        normalized_route = normalize_route_name(route) if normalize else route
        cache_key = normalized_route.lower()
        if use_cache:
            cached_response = ROUTE_CACHE.get(cache_key)
            if cached_response is not None:
                return cached_response

        params = {"route": normalized_route}
        response = await fetch_json(client, "TransitView/", params=params)

        if use_cache:
            ROUTE_CACHE.set(cache_key, response)

        return response
