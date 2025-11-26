"""Tool registration helpers for SEPTA MCP endpoints."""

from mcp.server.fastmcp import FastMCP

from .alerts_basic import register as register_alerts_basic
from .alerts_messages import register as register_alerts_messages
from .arrivals import register as register_arrivals
from .bus_detours import register as register_bus_detours
from .bus_schedule import register as register_bus_schedule
from .elevator_outages import register as register_elevator_outages
from .gtfs_feeds import register as register_gtfs_feeds
from .locations import register as register_locations
from .next_to_arrive import register as register_next_to_arrive
from .rr_schedule import register as register_rr_schedule
from .sms_schedule import register as register_sms_schedule
from .stops import register as register_stops
from .train_view import register as register_train_view
from .transit_view import register as register_transit_view
from .transit_view_all import register as register_transit_view_all
from .http import SeptaHttpClient


__all__ = [
    "register_all",
    "FastMCP",
    "SeptaHttpClient",
]


def register_all(server: FastMCP, client: SeptaHttpClient) -> None:
    """Register all SEPTA MCP tools on the provided server."""

    register_arrivals(server, client)
    register_next_to_arrive(server, client)
    register_train_view(server, client)
    register_transit_view(server, client)
    register_transit_view_all(server, client)
    register_bus_detours(server, client)
    register_alerts_basic(server, client)
    register_alerts_messages(server, client)
    register_elevator_outages(server, client)
    register_rr_schedule(server, client)
    register_bus_schedule(server, client)
    register_sms_schedule(server, client)
    register_stops(server, client)
    register_locations(server, client)
    register_gtfs_feeds(server, client)
