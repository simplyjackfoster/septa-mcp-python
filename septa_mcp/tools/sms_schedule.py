"""Tool for the SEPTA SMS schedule endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the SMS schedule tool on the server."""

    @server.tool(
        name="sms_schedule",
        description="Retrieve schedule data formatted for SMS stop lookups.",
        input_schema={
            "type": "object",
            "properties": {
                "req1": {
                    "type": "string",
                    "description": "Stop identifier or SMS code (API parameter req1).",
                },
                "req2": {
                    "type": "string",
                    "description": "Route identifier to limit the lookup (API parameter req2).",
                },
                "req3": {
                    "type": "string",
                    "description": "Direction for the requested stop (API parameter req3).",
                },
            },
            "required": ["req1"],
        },
    )
    async def sms_schedule_tool(
        req1: str, req2: str | None = None, req3: str | None = None
    ) -> object:
        params: dict[str, str] = {"req1": req1}
        if req2:
            params["req2"] = req2
        if req3:
            params["req3"] = req3

        return await fetch_json(client, "SMSSchedules/", params=params)
