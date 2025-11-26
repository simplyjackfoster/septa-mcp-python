"""Tool for the SEPTA TransitViewAll endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the TransitViewAll tool on the server."""

    @server.tool(
        name="transit_view_all",
        description="Return vehicle locations for all bus routes via the TransitViewAll feed.",
        input_schema={"type": "object", "properties": {}},
    )
    async def transit_view_all_tool() -> object:
        return await fetch_json(client, "TransitViewAll/", params=None)
