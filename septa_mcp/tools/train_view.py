"""Tool for the SEPTA TrainView endpoint."""

from __future__ import annotations

from .http import FastMCP, SeptaHttpClient, fetch_json


def register(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register the TrainView tool on the server."""

    @server.tool(
        name="train_view",
        description="Return real-time train data, optionally filtered by train or line.",
        input_schema={
            "type": "object",
            "properties": {
                "train_id": {
                    "type": "string",
                    "description": "Optional specific train identifier to filter results.",
                },
                "line": {
                    "type": "string",
                    "description": "Optional line or route name to narrow the response.",
                },
            },
        },
    )
    async def train_view_tool(
        train_id: str | None = None, line: str | None = None
    ) -> object:
        params: dict[str, str] = {}
        if train_id:
            params["train_id"] = train_id
        if line:
            params["line"] = line

        return await fetch_json(client, "TrainView/", params=params or None)
