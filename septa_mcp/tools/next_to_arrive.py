"""Tool for the SEPTA Next to Arrive endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the Next to Arrive tool on the server."""

    @server.tool(
        name="next_to_arrive",
        description=(
            "Retrieve the next available trips between an origin and destination using "
            "the Next to Arrive endpoint."
        ),
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
                    "description": "Optional date/time string for the planned departure (API parameter req3).",
                },
                "req4": {
                    "type": "string",
                    "description": "Optional travel preference or additional filter (API parameter req4).",
                },
            },
            "required": ["req1", "req2"],
        },
    )
    async def next_to_arrive_tool(
        req1: str, req2: str, req3: str | None = None, req4: str | None = None
    ) -> object:
        params: dict[str, str] = {"req1": req1, "req2": req2}
        if req3:
            params["req3"] = req3
        if req4:
            params["req4"] = req4

        return await fetch_json(client, "NextToArrive/", params=params)
