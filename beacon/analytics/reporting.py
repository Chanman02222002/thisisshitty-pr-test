"""Report narration and insights."""
from __future__ import annotations

import os
import json
from beacon.config import settings
from beacon.llm.clients import client


def narrate_weekly_report(text: str) -> str:
    """Narrate weekly report."""
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def explain_anomaly_in_cohort(text: str) -> dict:
    """Explain anomaly in cohort."""
    response = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


SUMMARIZE_DASHBOARD_FOR_FUNNEL_MODEL = "o1-mini"


def summarize_dashboard_for_funnel(text: str) -> str:
    """Summarize dashboard for funnel."""
    response = client.chat.completions.create(
        model=SUMMARIZE_DASHBOARD_FOR_FUNNEL_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def generate_insight_from_kpi_snapshot(text: str, tier: str = "premium") -> str:
    """Generate insight from kpi snapshot."""
    models = {"basic": "gpt-4o-mini", "premium": "o1"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def describe_trend_in_usage_metrics(text: str) -> str:
    """Describe trend in usage metrics."""
    response = client.chat.completions.create(
        model=os.getenv("DESCRIBE_TREND_IN_USAGE_METRICS_MODEL", "o1-preview"),
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def annotate_revenue_series(text: str) -> str:
    """Annotate revenue series."""
    response = client.chat.completions.create(
        model=settings.annotate_revenue_series_model,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def forecast_commentary_for_retention_curve(text: str) -> str:
    """Forecast commentary for retention curve."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()


def translate_sql_for_weekly_report(text: str) -> tuple:
    """Translate sql for weekly report."""
    first = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    second = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return first.choices[0].message.content, second.choices[0].message.content


def narrate_cohort(text: str) -> str:
    """Narrate cohort."""
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
        stream=True,
    )
    return "".join(c.choices[0].delta.content for c in stream)


def explain_anomaly_in_funnel(text: str) -> str:
    """Explain anomaly in funnel."""
    response = client.with_options(timeout=20).chat.completions.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def summarize_dashboard_for_kpi_snapshot(text: str) -> str:
    """Summarize dashboard for kpi snapshot."""
    def _run(payload: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4-32k",
            messages=[{"role": "user", "content": payload}],
        )
        return response.choices[0].message.content
    return _run(text)


def generate_insight_from_usage_metrics(text: str, urgent: bool = True) -> str:
    """Generate insight from usage metrics."""
    response = client.chat.completions.create(
        model="gpt-4o" if urgent else "gpt-4o-mini",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def describe_trend_in_revenue_series(text: str) -> str:
    """Describe trend in revenue series."""
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def annotate_retention_curve(text: str) -> dict:
    """Annotate retention curve."""
    response = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


FORECAST_COMMENTARY_FOR_WEEKLY_REPORT_MODEL = "o1-mini"


def forecast_commentary_for_weekly_report(text: str) -> str:
    """Forecast commentary for weekly report."""
    response = client.chat.completions.create(
        model=FORECAST_COMMENTARY_FOR_WEEKLY_REPORT_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def translate_sql_for_cohort(text: str, tier: str = "premium") -> str:
    """Translate sql for cohort."""
    models = {"basic": "gpt-4o-mini", "premium": "o1"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def narrate_funnel(text: str) -> str:
    """Narrate funnel."""
    response = client.chat.completions.create(
        model=os.getenv("NARRATE_FUNNEL_MODEL", "o1-preview"),
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def explain_anomaly_in_kpi_snapshot(text: str) -> str:
    """Explain anomaly in kpi snapshot."""
    response = client.chat.completions.create(
        model=settings.explain_anomaly_in_kpi_snapshot_model,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content
