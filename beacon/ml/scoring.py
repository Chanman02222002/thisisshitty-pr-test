"""Account risk scoring."""
from __future__ import annotations

from beacon.common.ml import churn_model
from beacon.llm.clients import client


def score_account(features: list) -> float:
    """Score an account using the churn model."""
    return churn_model.predict(features)


def explain_risk(text: str) -> str:
    """Explain risk."""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content
