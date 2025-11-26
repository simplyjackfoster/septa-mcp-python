"""Tool for the SEPTA regional rail schedule endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the regional rail schedule tool on the server."""

    @server.tool(
        name="rr_schedule",
        description="Look up a regional rail timetable between an origin and destination.",
        input_schema={
            "type": "object",
            "properties": {
                "req1": {
                    "type": "string",
                    "description": "Origin station or stop name (API parameter req1).",
                },
                "req2": {
                    "type": "string",
                    "description": "Destination station or stop name (API parameter req2).",
                },
                "req3": {
                    "type": "string",
                    "description": "Optional date/time string for schedule lookups (API parameter req3).",
                },
            },
            "required": ["req1", "req2"],
        },
    )
    async def rr_schedule_tool(req1: str, req2: str, req3: str | None = None) -> object:
        params: dict[str, str] = {"req1": req1, "req2": req2}
        if req3:
            params["req3"] = req3

        return await fetch_json(client, "RRSchedule/", params=params)
