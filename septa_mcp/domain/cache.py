"""Lightweight in-memory TTL cache for frequently used responses."""

from __future__ import annotations

import time
from typing import Generic, Hashable, MutableMapping, TypeVar

T = TypeVar("T")


class TTLCache(Generic[T]):
    """A simple time-based cache for short-lived responses."""

    def __init__(self, ttl_seconds: float) -> None:
        self._ttl_seconds = ttl_seconds
        self._store: MutableMapping[Hashable, tuple[float, T]] = {}

    def get(self, key: Hashable) -> T | None:
        """Retrieve a cached value if it has not expired."""

        item = self._store.get(key)
        if item is None:
            return None

        expires_at, value = item
        if expires_at < time.monotonic():
            self._store.pop(key, None)
            return None

        return value

    def set(self, key: Hashable, value: T) -> None:
        """Store a value in the cache."""

        self._store[key] = (time.monotonic() + self._ttl_seconds, value)

    def clear(self) -> None:
        """Empty the cache."""

        self._store.clear()


__all__ = ["TTLCache"]
