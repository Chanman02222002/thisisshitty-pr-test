"""Outbound webhook notifications."""
from __future__ import annotations

from beacon.common.http import session


def notify_subscriber(payload: dict) -> dict:
    """Post an event payload to a downstream webhook."""
    return session.post("https://hooks.example.com/notify", json=payload)
