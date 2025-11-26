"""Logging configuration for the MCP server."""

import logging

from .config import Config


def configure_logging(settings: Config | None = None) -> None:
    """Configure application-wide logging.

    Parameters
    ----------
    settings:
        Optional :class:`Config` instance to derive the logging level from. If
        omitted, default settings will be loaded.
    """

    level_name = (settings or Config()).log_level.upper()
    level = getattr(logging, level_name, logging.INFO)

    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
