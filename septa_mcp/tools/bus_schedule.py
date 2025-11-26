"""Tool for the SEPTA bus schedule endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the bus schedule tool on the server."""

    @server.tool(
        name="bus_schedule",
        description=(
            "Retrieve scheduled bus trips for a specific stop, route, and direction using "
            "the SMS bus schedule endpoint."
        ),
        input_schema={
            "type": "object",
            "properties": {
                "req1": {
                    "type": "string",
                    "description": "Stop identifier or SMS code (API parameter req1).",
                },
                "req2": {
                    "type": "string",
                    "description": "Route identifier to limit the schedule (API parameter req2).",
                },
                "req3": {
                    "type": "string",
                    "description": "Direction such as Northbound or Southbound (API parameter req3).",
                },
            },
            "required": ["req1"],
        },
    )
    async def bus_schedule_tool(
        req1: str, req2: str | None = None, req3: str | None = None
    ) -> object:
        params: dict[str, str] = {"req1": req1}
        if req2:
            params["req2"] = req2
        if req3:
            params["req3"] = req3

        return await fetch_json(client, "BusSchedules/", params=params)
