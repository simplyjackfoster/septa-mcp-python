"""Registration logic for the MCP server."""

import logging

from .http_client import HttpClient

logger = logging.getLogger(__name__)


async def register_server(client: HttpClient) -> None:
    """Placeholder registration step for the MCP server."""

    logger.info("Registering SEPTA MCP server with configured backend")
    # This placeholder can be expanded to register tools or capabilities.
    await client.get("/")
    logger.info("Registration completed")
