"""Helpers for normalizing station and route identifiers."""

from __future__ import annotations

from typing import Mapping


StationAliasMap = Mapping[str, str]
RouteAliasMap = Mapping[str, str]


STATION_ALIASES: dict[str, str] = {
    "30th st": "30th Street Station",
    "30th street": "30th Street Station",
    "30th street station": "30th Street Station",
    "jefferson": "Jefferson Station",
    "market east": "Jefferson Station",
    "suburban": "Suburban Station",
    "suburban station": "Suburban Station",
}

ROUTE_ALIASES: dict[str, str] = {
    "bsl": "Broad Street Line",
    "bss": "Broad Street Line",
    "broad street": "Broad Street Line",
    "broad street line": "Broad Street Line",
    "mfl": "Market-Frankford Line",
    "market frankford": "Market-Frankford Line",
    "market-frankford": "Market-Frankford Line",
    "market-frankford line": "Market-Frankford Line",
    "nhsl": "Norristown High Speed Line",
    "norristown high speed": "Norristown High Speed Line",
    "norristown high speed line": "Norristown High Speed Line",
    "airport": "Airport Line",
    "airport line": "Airport Line",
}


def _normalize_value(value: str, aliases: Mapping[str, str]) -> str:
    key = value.strip().lower()
    return aliases.get(key, value.strip())


def normalize_station_name(name: str, aliases: StationAliasMap | None = None) -> str:
    """Normalize a station name using known aliases.

    Parameters
    ----------
    name:
        The user-provided station or stop identifier.
    aliases:
        Optional alias map. Defaults to :data:`STATION_ALIASES`.
    """

    return _normalize_value(name, aliases or STATION_ALIASES)


def normalize_route_name(name: str, aliases: RouteAliasMap | None = None) -> str:
    """Normalize a route or line identifier using known aliases.

    Parameters
    ----------
    name:
        The user-provided route or line identifier.
    aliases:
        Optional alias map. Defaults to :data:`ROUTE_ALIASES`.
    """

    return _normalize_value(name, aliases or ROUTE_ALIASES)


__all__ = [
    "ROUTE_ALIASES",
    "STATION_ALIASES",
    "normalize_route_name",
    "normalize_station_name",
]
