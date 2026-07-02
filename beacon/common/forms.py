"""Form definition builder for the intake UI."""
from __future__ import annotations

from typing import Any


class _FormBuilder:
    def create(self, model: str, fields: Any) -> dict[str, Any]:
        return {"model": model, "fields": list(fields), "id": "form_1"}


form_builder = _FormBuilder()
