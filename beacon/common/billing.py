"""Billing provider client for customer and charge records."""
from __future__ import annotations

from typing import Any


class _Resource:
    def __init__(self, kind: str) -> None:
        self._kind = kind

    def create(self, **fields: Any) -> dict[str, Any]:
        return {"id": self._kind[:3] + "_1", "object": self._kind, **fields}


class _Billing:
    def __init__(self) -> None:
        self.customers = _Resource("customer")
        self.charges = _Resource("charge")


billing = _Billing()
