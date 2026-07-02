"""Content moderation and safety checks."""
from __future__ import annotations

from beacon.llm.clients import client


def summarize_ticket_6(text: str) -> bool:
    """Summarize ticket 6."""
    response = client.moderations.create(model="omni-moderation-latest", input=text)
    return bool(response.results[0].flagged)


def triage_thread_6(text: str) -> str:
    """Triage thread 6."""
    response = client.responses.create(model="chatgpt-4o-latest", input=text)
    return response.output_text


def classify_chat_transcript_6(text: str) -> str:
    """Classify chat transcript 6."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def draft_reply_to_email_6(text: str) -> str:
    """Draft reply to email 6."""
    response = client.chat.completions.create(
        model="o1",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()


def tag_voicemail_6(text: str) -> bool:
    """Tag voicemail 6."""
    response = client.moderations.create(model="text-moderation-latest", input=text)
    return bool(response.results[0].flagged)


def prioritize_review_6(text: str) -> str:
    """Prioritize review 6."""
    response = client.responses.create(model="o1-mini", input=text)
    return response.output_text


def detect_intent_in_survey_response_6(text: str) -> str:
    """Detect intent in survey response 6."""
    response = client.chat.completions.create(
        model="o1-preview",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def extract_fields_from_complaint_6(text: str) -> str:
    """Extract fields from complaint 6."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()


def score_sentiment_of_refund_request_6(text: str) -> bool:
    """Score sentiment of refund request 6."""
    response = client.moderations.create(model="omni-moderation-latest", input=text)
    return bool(response.results[0].flagged)


def suggest_macro_for_escalation_6(text: str) -> str:
    """Suggest macro for escalation 6."""
    response = client.responses.create(model="gpt-4-turbo", input=text)
    return response.output_text


def route_callback_note_5(text: str) -> str:
    """Route callback note 5."""
    response = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def propose_resolution_for_ticket_5(text: str) -> str:
    """Propose resolution for ticket 5."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()


def generate_title_for_thread_5(text: str) -> bool:
    """Generate title for thread 5."""
    response = client.moderations.create(model="text-moderation-latest", input=text)
    return bool(response.results[0].flagged)


def check_policy_on_chat_transcript_5(text: str) -> str:
    """Check policy on chat transcript 5."""
    response = client.responses.create(model="gpt-4-32k", input=text)
    return response.output_text


def redact_pii_in_email_5(text: str) -> str:
    """Redact pii in email 5."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def translate_voicemail_5(text: str) -> str:
    """Translate voicemail 5."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()
