"""Registration logic for the MCP server."""

import logging

from mcp.server.fastmcp import FastMCP

from .http_client import HttpClient
from .tools import register_all

logger = logging.getLogger(__name__)


async def register_server(client: HttpClient) -> FastMCP:
    """Register all SEPTA MCP tools on a server instance."""

    logger.info("Registering SEPTA MCP server with configured backend")
    server = FastMCP("septa-mcp")
    register_all(server, client)
    logger.info("Registration completed")
    return server
