"""Tool for the SEPTA alert messages endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the alert messages tool on the server."""

    @server.tool(
        name="alerts_messages",
        description="Retrieve detailed alert messages optionally filtered by route or mode.",
        input_schema={
            "type": "object",
            "properties": {
                "route": {
                    "type": "string",
                    "description": "Optional route identifier to narrow alert messages.",
                },
                "mode": {
                    "type": "string",
                    "description": "Optional transit mode such as rail, bus, or trolley.",
                },
            },
        },
    )
    async def alerts_messages_tool(route: str | None = None, mode: str | None = None) -> object:
        params: dict[str, str] = {}
        if route:
            params["route"] = route
        if mode:
            params["mode"] = mode

        return await fetch_json(client, "alerts/messages.php", params=params or None)
