"""Tool for the SEPTA stops endpoint."""

from __future__ import annotations

from ..domain.normalization import normalize_route_name
from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the stops tool on the server."""

    @server.tool(
        name="stops",
        description="List stops for a given route and direction or lookup a specific stop id.",
        input_schema={
            "type": "object",
            "properties": {
                "route": {
                    "type": "string",
                    "description": "Route identifier whose stops should be returned.",
                },
                "direction": {
                    "type": "string",
                    "description": "Optional travel direction for the route (API parameter dir).",
                },
                "stop_id": {
                    "type": "string",
                    "description": "Optional stop id to retrieve if known instead of listing all stops.",
                },
                "normalize": {
                    "type": "boolean",
                    "description": "Normalize the route name using common aliases before querying.",
                    "default": True,
                },
            },
        },
    )
    async def stops_tool(
        route: str | None = None,
        direction: str | None = None,
        stop_id: str | None = None,
        normalize: bool = True,
    ) -> object:
        params: dict[str, str] = {}
        if route:
            params["route"] = normalize_route_name(route) if normalize else route
        if direction:
            params["dir"] = direction
        if stop_id:
            params["stop_id"] = stop_id

        return await fetch_json(client, "Stops/", params=params or None)
