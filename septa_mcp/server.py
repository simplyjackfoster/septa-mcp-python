"""Entry point for launching the MCP server."""

import asyncio
import logging

from .config import get_settings
from .http_client import create_http_client
from .logging_config import configure_logging
from .registration import register_server

logger = logging.getLogger(__name__)


def main() -> None:
    """Console script entrypoint for the MCP server."""

    settings = get_settings()
    configure_logging(settings)
    logger.info("Starting SEPTA MCP server")

    asyncio.run(run_server())


async def run_server() -> None:
    """Run the MCP server lifecycle."""

    settings = get_settings()
    client = await create_http_client(settings)
    try:
        await register_server(client)
    finally:
        await client.close()
