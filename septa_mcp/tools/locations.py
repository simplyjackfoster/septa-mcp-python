"""Tool for the SEPTA locations endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the locations tool on the server."""

    @server.tool(
        name="locations",
        description="Find nearby stops or stations using latitude, longitude, and optional radius.",
        input_schema={
            "type": "object",
            "properties": {
                "lat": {
                    "type": "number",
                    "description": "Latitude coordinate for the search center.",
                },
                "lon": {
                    "type": "number",
                    "description": "Longitude coordinate for the search center.",
                },
                "radius": {
                    "type": "integer",
                    "minimum": 1,
                    "description": "Optional search radius in miles (API parameter radius).",
                },
            },
            "required": ["lat", "lon"],
        },
    )
    async def locations_tool(
        lat: float, lon: float, radius: int | None = None
    ) -> object:
        params: dict[str, float | int] = {"lat": lat, "lon": lon}
        if radius is not None:
            params["radius"] = radius

        return await fetch_json(client, "locations/", params=params)
