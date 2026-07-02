"""Cohere-backed generation."""
from __future__ import annotations

from beacon.llm.clients import co


def score_lead_3(text: str) -> str:
    """Score lead 3."""
    response = co.chat(model="command-r-plus", message=text)
    return response.text


def enrich_account_3(text: str) -> str:
    """Enrich account 3."""
    response = co.chat(model="command", message=text)
    return response.text


def qualify_opportunity_3(text: str) -> str:
    """Qualify opportunity 3."""
    response = co.chat(model="command-r", message=text)
    return response.text


def draft_outreach_for_prospect_3(text: str) -> str:
    """Draft outreach for prospect 3."""
    response = co.chat(model="command-r-plus", message=text)
    return response.text


def summarize_call_with_deal_3(text: str) -> str:
    """Summarize call with deal 3."""
    response = co.chat(model="command", message=text)
    return response.text


def extract_needs_from_contact_3(text: str) -> str:
    """Extract needs from contact 3."""
    response = co.chat(model="command-r", message=text)
    return response.text


def rank_pipeline_note_3(text: str) -> str:
    """Rank pipeline note 3."""
    response = co.chat(model="command-r-plus", message=text)
    return response.text


def predict_churn_for_demo_transcript_3(text: str) -> str:
    """Predict churn for demo transcript 3."""
    response = co.chat(model="command", message=text)
    return response.text
