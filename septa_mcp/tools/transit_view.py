"""Tool for the SEPTA TransitView endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


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
                }
            },
            "required": ["route"],
        },
    )
    async def transit_view_tool(route: str) -> object:
        params = {"route": route}
        return await fetch_json(client, "TransitView/", params=params)
