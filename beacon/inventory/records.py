"""Inventory and record persistence."""
from __future__ import annotations

from beacon.common.db import db


def persist_inventory(warehouse: str) -> dict:
    """Persist inventory rows for a warehouse."""
    row = db.records.create(model=warehouse, quantity=12)
    idx = db.embeddings.create(vector_id="v-1", dim=768)
    return {"row": row, "index": idx}


def open_ticket(subject: str) -> dict:
    """Open a support ticket record."""
    return db.tickets.create(model="standard", subject=subject, status="open")
