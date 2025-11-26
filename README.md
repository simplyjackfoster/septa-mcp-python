# SEPTA MCP Server (Python)

This repository provides a Model Context Protocol (MCP) server that exposes SEPTA's public transit APIs as structured tools. It lets MCP-compatible clients fetch realtime and scheduled information about buses, trolleys, subways, and Regional Rail through a consistent interface.

## Installation

1. Ensure Python 3.11+ is available.
2. Install the package (use the optional dev extras if you plan to contribute):
   ```bash
   pip install -e .[dev]
   ```
3. Start the server via the console script:
   ```bash
   septa-mcp
   ```

## Configuration

Configuration is driven by environment variables with the `SEPTA_` prefix:

- `SEPTA_BASE_URL` (default: `https://www3.septa.org/`): Base URL for all SEPTA API requests.
- `SEPTA_TIMEOUT_SECONDS` (default: `10.0`): Timeout in seconds for HTTP requests.
- `SEPTA_LOG_LEVEL` (default: `INFO`): Logging verbosity for the server.
- `SEPTA_API_KEY` (optional): API key passed as a bearer token when required.

## Available tools

The server registers the following tools (names match the MCP tool identifiers):

- **arrivals**: Upcoming arrivals for a station with optional direction and time window.
- **next_to_arrive**: Next available trips between an origin and destination, with optional datetime and travel preferences.
- **train_view**: Real-time Regional Rail train data, filterable by train or line.
- **transit_view**: Real-time vehicle locations for a specific bus route, with caching to limit repeat requests.
- **transit_view_all**: Real-time vehicle locations for all bus routes, optionally cached briefly.
- **bus_detours**: Current detours for all bus routes or a specific route.
- **alerts_basic**: Basic service alerts, optionally limited to a route.
- **alerts_messages**: Detailed alert messages, optionally filtered by route or mode.
- **elevator_outages**: System-wide elevator outage information.
- **rr_schedule**: Regional Rail timetables between an origin and destination, with optional datetime.
- **bus_schedule**: Scheduled bus trips for a stop/route/direction via the SMS bus schedule endpoint.
- **sms_schedule**: SMS-formatted schedule data for a stop, with optional route and direction filters.
- **stops**: Stop listing for a route/direction or lookup by stop id, with optional route normalization.
- **locations**: Nearby stops or stations based on latitude/longitude and optional radius.
- **gtfs_feed**: Downloadable GTFS feed archives such as `google`, `google_bus`, `google_rail`, or `cct`.

## Example prompts

Use natural language to trigger the MCP tools in your client. Examples:

- "Show arrivals at 30th Street Station heading east in the next 20 minutes."
- "Find the next trains from Suburban Station to Trenton after 5pm."
- "List current bus detours for route 17." 
- "Get TransitView data for route 47 and cache the response."
- "Download the latest `google_rail` GTFS feed."

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidance on development workflow, style, tests, and CI expectations.
