"""Tool for the SEPTA Next to Arrive endpoint."""

from __future__ import annotations

from ..domain.normalization import normalize_station_name
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
                "normalize": {
                    "type": "boolean",
                    "description": "Normalize origin and destination names using common aliases.",
                    "default": True,
                },
            },
            "required": ["req1", "req2"],
        },
    )
    async def next_to_arrive_tool(
        req1: str,
        req2: str,
        req3: str | None = None,
        req4: str | None = None,
        normalize: bool = True,
    ) -> object:
        origin = normalize_station_name(req1) if normalize else req1
        destination = normalize_station_name(req2) if normalize else req2
        params: dict[str, str] = {"req1": origin, "req2": destination}
        if req3:
            params["req3"] = req3
        if req4:
            params["req4"] = req4

        return await fetch_json(client, "NextToArrive/", params=params)
