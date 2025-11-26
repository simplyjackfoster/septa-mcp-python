"""Tool for the SEPTA BusDetours endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the BusDetours tool on the server."""

    @server.tool(
        name="bus_detours",
        description="Retrieve detour information for all bus routes or a specific route.",
        input_schema={
            "type": "object",
            "properties": {
                "route": {
                    "type": "string",
                    "description": "Optional bus route identifier to filter detours.",
                }
            },
        },
    )
    async def bus_detours_tool(route: str | None = None) -> object:
        params = {"route": route} if route else None
        return await fetch_json(client, "BusDetours/", params=params)
