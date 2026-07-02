"""Outbound HTTP helper for webhook notifications."""
from __future__ import annotations

from typing import Any


class _Session:
    def post(self, url: str, **kwargs: Any) -> dict[str, Any]:
        return {"url": url, "status_code": 200, "sent": kwargs}

    def get(self, url: str, **kwargs: Any) -> dict[str, Any]:
        return {"url": url, "status_code": 200}


session = _Session()
