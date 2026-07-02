"""Intake form construction."""
from __future__ import annotations

from beacon.common.forms import form_builder


def build_form(kind: str) -> dict:
    """Builds a UI form definition."""
    return form_builder.create(model=kind, fields=["name", "email"])
