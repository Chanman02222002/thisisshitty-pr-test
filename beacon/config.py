"""Application settings for the Beacon backend."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Settings:
    annotate_revenue_series_model: str = "gpt-4o-mini"
    explain_anomaly_in_kpi_snapshot_model: str = "gpt-4o-mini"
    extract_needs_from_contact_model: str = "gpt-3.5-turbo"
    generate_subject_lines_for_case_study_model: str = "gpt-3.5-turbo"
    generate_subject_lines_for_press_release_model: str = "gpt-3.5-turbo"
    prioritize_review_model: str = "gpt-3.5-turbo"
    rank_renewal_model: str = "gpt-3.5-turbo"
    triage_survey_response_model: str = "gpt-3.5-turbo"
    environment: str = "production"


settings = Settings()
