"""Tool for downloading SEPTA GTFS feeds."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the GTFS feed tool on the server."""

    @server.tool(
        name="gtfs_feed",
        description=(
            "Download a GTFS feed (zip) such as google, google_rail, google_bus, or cct. "
            "The feed parameter is appended to /gtfs/{feed}.zip."
        ),
        input_schema={
            "type": "object",
            "properties": {
                "feed": {
                    "type": "string",
                    "description": "Feed name to download (e.g., google, google_rail, google_bus, cct).",
                }
            },
            "required": ["feed"],
        },
    )
    async def gtfs_feed_tool(feed: str) -> bytes:
        path = f"gtfs/{feed}.zip"
        response = await client.get(path)
        return response.content
