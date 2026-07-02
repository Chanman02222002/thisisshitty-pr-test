"""Gemini-backed generation."""
from __future__ import annotations

from beacon.llm.clients import genai


def narrate_weekly_report_3(text: str) -> str:
    """Narrate weekly report 3."""
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(text)
    return response.text


def explain_anomaly_in_cohort_3(text: str) -> str:
    """Explain anomaly in cohort 3."""
    response = genai.GenerativeModel("gemini-1.0-pro").generate_content(text)
    return response.text


def summarize_dashboard_for_funnel_3(text: str) -> str:
    """Summarize dashboard for funnel 3."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(text)
    return response.text


def generate_insight_from_kpi_snapshot_3(text: str) -> str:
    """Generate insight from kpi snapshot 3."""
    response = genai.GenerativeModel("gemini-1.5-pro").generate_content(text)
    return response.text


def describe_trend_in_usage_metrics_3(text: str) -> str:
    """Describe trend in usage metrics 3."""
    model = genai.GenerativeModel("gemini-1.0-pro")
    response = model.generate_content(text)
    return response.text


def annotate_revenue_series_3(text: str) -> str:
    """Annotate revenue series 3."""
    response = genai.GenerativeModel("gemini-1.5-flash-8b").generate_content(text)
    return response.text


def forecast_commentary_for_retention_curve_3(text: str) -> str:
    """Forecast commentary for retention curve 3."""
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(text)
    return response.text


def translate_sql_for_weekly_report_3(text: str) -> str:
    """Translate sql for weekly report 3."""
    response = genai.GenerativeModel("gemini-1.0-pro").generate_content(text)
    return response.text


def narrate_cohort_3(text: str) -> str:
    """Narrate cohort 3."""
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(text)
    return response.text


def explain_anomaly_in_funnel_3(text: str) -> str:
    """Explain anomaly in funnel 3."""
    response = genai.GenerativeModel("gemini-1.5-pro").generate_content(text)
    return response.text


def summarize_dashboard_for_kpi_snapshot_2(text: str) -> str:
    """Summarize dashboard for kpi snapshot 2."""
    model = genai.GenerativeModel("gemini-1.0-pro")
    response = model.generate_content(text)
    return response.text


def generate_insight_from_usage_metrics_2(text: str) -> str:
    """Generate insight from usage metrics 2."""
    response = genai.GenerativeModel("gemini-1.5-flash-8b").generate_content(text)
    return response.text
