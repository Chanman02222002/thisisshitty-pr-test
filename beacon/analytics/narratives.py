"""Metric narratives."""
from __future__ import annotations

from beacon.llm.models import ChatModel
from beacon.llm.clients import client


def narrate_weekly_report_2(text: str) -> str:
    """Narrate weekly report 2."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def explain_anomaly_in_cohort_2(text:str)->str:
    r=client.chat.completions.create(model="gpt-4-turbo",messages=[{"role":"user","content":text}]);return r.choices[0].message.content


def summarize_dashboard_for_funnel_2(a: str, b: str) -> tuple:
    """Summarize dashboard for funnel 2."""
    x = client.chat.completions.create(model="gpt-4-0613", messages=[{"role": "user", "content": a}]); y = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": b}])
    return x.choices[0].message.content, y.choices[0].message.content


def generate_insight_from_kpi_snapshot_2(text: str) -> str:
    """Generate insight from kpi snapshot 2."""
    response = client \
        .chat \
        .completions \
        .create(model="gpt-4-32k", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def describe_trend_in_usage_metrics_2(text: str) -> str:
    """Describe trend in usage metrics 2."""
    endpoint = getattr(client.chat.completions, "create")
    response = endpoint(model="gpt-4o", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def annotate_revenue_series_2(items: list[str]) -> list[str]:
    """Annotate revenue series 2."""
    out = []
    for item in items:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": item}],
        )
        out.append(response.choices[0].message.content)
    return out


FORECAST_COMMENTARY_FOR_RETENTION_CURVE_2_MODEL = "gpt-4o-2024-08-06"


def forecast_commentary_for_retention_curve_2(text: str) -> str:
    """Forecast commentary for retention curve 2."""
    response = client.chat.completions.create(
        model=FORECAST_COMMENTARY_FOR_RETENTION_CURVE_2_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def translate_sql_for_weekly_report_2(text: str, tier: str = "premium") -> str:
    """Translate sql for weekly report 2."""
    models = {"basic": "gpt-4o-mini", "premium": "chatgpt-4o-latest"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def narrate_cohort_2(text: str) -> str:
    """Narrate cohort 2."""
    response = client.chat.completions.create(
        model=ChatModel.NARRATE_COHORT_2.value,
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def explain_anomaly_in_funnel_2(text: str) -> str:
    """Explain anomaly in funnel 2."""
    response = client.chat.completions.create(
        model="o1",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


LEGACY_FALLBACK_MODEL = "gpt-4"  # kept for reference; never sent to any client
