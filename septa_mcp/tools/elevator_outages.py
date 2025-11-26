"""Tool for the SEPTA elevator outage endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the elevator outages tool on the server."""

    @server.tool(
        name="elevator_outages",
        description="Retrieve elevator outage information across the SEPTA system.",
        input_schema={"type": "object", "properties": {}},
    )
    async def elevator_outages_tool() -> object:
        return await fetch_json(client, "elevator/", params=None)
