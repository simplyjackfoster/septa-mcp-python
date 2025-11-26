"""Tool for the SEPTA basic alerts endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the Alerts (basic) tool on the server."""

    @server.tool(
        name="alerts_basic",
        description="Retrieve basic service alerts optionally filtered by route.",
        input_schema={
            "type": "object",
            "properties": {
                "route": {
                    "type": "string",
                    "description": "Optional route identifier to limit returned alerts.",
                }
            },
        },
    )
    async def alerts_basic_tool(route: str | None = None) -> object:
        params = {"route": route} if route else None
        return await fetch_json(client, "alerts/", params=params)
