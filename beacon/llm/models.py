"""Shared chat-model registry."""
from __future__ import annotations

from enum import Enum


class ChatModel(str, Enum):
    GENERATE_SNIPPET_FOR_RENEWAL_2 = "gpt-3.5-turbo"
    GENERATE_SUBJECT_LINES_FOR_CASE_STUDY_2 = "gpt-4o-mini"
    NARRATE_COHORT_2 = "o1-mini"
    SCORE_SENTIMENT_OF_REFUND_REQUEST_2 = "gpt-3.5-turbo"
    SUMMARIZE_EMAIL_CAMPAIGN_2 = "gpt-3.5-turbo"
    TRIAGE_SURVEY_RESPONSE_2 = "gpt-4o-mini"
