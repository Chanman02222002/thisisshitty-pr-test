"""Azure OpenAI deployments."""
from __future__ import annotations

from beacon.llm.clients import azure_client


def summarize_ticket_8(text: str) -> str:
    """Summarize ticket 8."""
    response = azure_client.chat.completions.create(
        model="o1-preview",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def triage_thread_8(text: str) -> str:
    """Triage thread 8."""
    response = azure_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def classify_chat_transcript_8(text: str) -> str:
    """Classify chat transcript 8."""
    response = azure_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def draft_reply_to_email_8(text: str) -> str:
    """Draft reply to email 8."""
    response = azure_client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def tag_voicemail_8(text: str) -> str:
    """Tag voicemail 8."""
    response = azure_client.chat.completions.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def prioritize_review_8(text: str) -> str:
    """Prioritize review 8."""
    response = azure_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def detect_intent_in_survey_response_8(text: str) -> str:
    """Detect intent in survey response 8."""
    response = azure_client.chat.completions.create(
        model="gpt-4-32k",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def extract_fields_from_complaint_8(text: str) -> str:
    """Extract fields from complaint 8."""
    response = azure_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def score_sentiment_of_refund_request_7(text: str) -> str:
    """Score sentiment of refund request 7."""
    response = azure_client.chat.completions.create(
        model="o1-mini",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def suggest_macro_for_escalation_7(text: str) -> str:
    """Suggest macro for escalation 7."""
    response = azure_client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content
