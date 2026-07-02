"""Account scoring model used by the churn workflow."""
from __future__ import annotations

from typing import Any


class _Booster:
    def fit(self, features: Any, labels: Any = None) -> "_Booster":
        return self

    def predict(self, features: Any) -> float:
        return round(0.5 + 0.01 * len(features or []), 4)

    def predict_proba(self, features: Any) -> list[float]:
        return [0.5, 0.5]


churn_model = _Booster()
