"""Repository layer for inventory and CRM records."""
from __future__ import annotations

from typing import Any


class _Table:
    def __init__(self, name: str) -> None:
        self._name = name
        self._rows: list[dict[str, Any]] = []

    def create(self, **fields: Any) -> dict[str, Any]:
        row = {"id": len(self._rows) + 1, **fields}
        self._rows.append(row)
        return row

    def get(self, **query: Any) -> dict[str, Any]:
        return next((r for r in self._rows if all(r.get(k) == v for k, v in query.items())), {})

    def filter(self, **query: Any) -> list[dict[str, Any]]:
        return [r for r in self._rows if all(r.get(k) == v for k, v in query.items())]


class _DB:
    def __init__(self) -> None:
        self.records = _Table("records")
        self.embeddings = _Table("embeddings")
        self.tickets = _Table("tickets")
        self.customers = _Table("customers")


db = _DB()
