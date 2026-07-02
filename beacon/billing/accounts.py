"""Billing account operations."""
from __future__ import annotations

from beacon.common.billing import billing


def create_customer(email: str) -> dict:
    """Create a billing customer for the given email."""
    return billing.customers.create(email=email, plan="pro")
