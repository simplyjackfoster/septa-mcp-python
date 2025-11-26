"""Tool for the SEPTA arrivals endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the arrivals tool on the server."""

    @server.tool(
        name="arrivals",
        description=(
            "Fetch upcoming arrivals for a station with optional direction and minute window."
        ),
        input_schema={
            "type": "object",
            "properties": {
                "station": {
                    "type": "string",
                    "description": "Station name or stop identifier used by the arrivals endpoint.",
                },
                "direction": {
                    "type": "string",
                    "description": "Optional direction filter such as 'N', 'S', 'E', or 'W'.",
                },
                "minutes": {
                    "type": "integer",
                    "minimum": 1,
                    "description": "Optional window in minutes for which to return upcoming service.",
                },
            },
            "required": ["station"],
        },
    )
    async def arrivals_tool(
        station: str, direction: str | None = None, minutes: int | None = None
    ) -> object:
        params: dict[str, object] = {"station": station}
        if direction:
            params["direction"] = direction
        if minutes is not None:
            params["minutes"] = minutes

        return await fetch_json(client, "arrivals", params=params)
