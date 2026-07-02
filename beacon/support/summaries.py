"""Support ticket summarization and field extraction."""
from __future__ import annotations

import os
import json
from beacon.config import settings
from beacon.llm.clients import client


def summarize_ticket(text: str) -> str:
    """Summarize ticket."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def triage_thread(text: str) -> dict:
    """Triage thread."""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


CLASSIFY_CHAT_TRANSCRIPT_MODEL = "gpt-4o-mini"


def classify_chat_transcript(text: str) -> str:
    """Classify chat transcript."""
    response = client.chat.completions.create(
        model=CLASSIFY_CHAT_TRANSCRIPT_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def draft_reply_to_email(text: str, tier: str = "premium") -> str:
    """Draft reply to email."""
    models = {"basic": "gpt-4o-mini", "premium": "gpt-4-0613"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def tag_voicemail(text: str) -> str:
    """Tag voicemail."""
    response = client.chat.completions.create(
        model=os.getenv("TAG_VOICEMAIL_MODEL", "gpt-4-32k"),
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def prioritize_review(text: str) -> str:
    """Prioritize review."""
    response = client.chat.completions.create(
        model=settings.prioritize_review_model,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def detect_intent_in_survey_response(text: str) -> str:
    """Detect intent in survey response."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()


def extract_fields_from_complaint(text: str) -> tuple:
    """Extract fields from complaint."""
    first = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    second = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return first.choices[0].message.content, second.choices[0].message.content


def score_sentiment_of_refund_request(text: str) -> str:
    """Score sentiment of refund request."""
    stream = client.chat.completions.create(
        model="o1-mini",
        messages=[{"role": "user", "content": text}],
        stream=True,
    )
    return "".join(c.choices[0].delta.content for c in stream)


def suggest_macro_for_escalation(text: str) -> str:
    """Suggest macro for escalation."""
    response = client.with_options(timeout=20).chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def route_callback_note(text: str) -> str:
    """Route callback note."""
    def _run(payload: str) -> str:
        response = client.chat.completions.create(
            model="o1",
            messages=[{"role": "user", "content": payload}],
        )
        return response.choices[0].message.content
    return _run(text)


def propose_resolution_for_ticket(text: str, urgent: bool = True) -> str:
    """Propose resolution for ticket."""
    response = client.chat.completions.create(
        model="o1-preview" if urgent else "gpt-4o-mini",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def generate_title_for_thread(text: str) -> str:
    """Generate title for thread."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def check_policy_on_chat_transcript(text: str) -> dict:
    """Check policy on chat transcript."""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


REDACT_PII_IN_EMAIL_MODEL = "gpt-4o-mini"


def redact_pii_in_email(text: str) -> str:
    """Redact pii in email."""
    response = client.chat.completions.create(
        model=REDACT_PII_IN_EMAIL_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def translate_voicemail(text: str, tier: str = "premium") -> str:
    """Translate voicemail."""
    models = {"basic": "gpt-4o-mini", "premium": "gpt-4-0613"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def summarize_review(text: str) -> str:
    """Summarize review."""
    response = client.chat.completions.create(
        model=os.getenv("SUMMARIZE_REVIEW_MODEL", "gpt-4-32k"),
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def triage_survey_response(text: str) -> str:
    """Triage survey response."""
    response = client.chat.completions.create(
        model=settings.triage_survey_response_model,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def classify_complaint(text: str) -> str:
    """Classify complaint."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()


def draft_reply_to_refund_request(text: str) -> tuple:
    """Draft reply to refund request."""
    first = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    second = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return first.choices[0].message.content, second.choices[0].message.content


def tag_escalation(text: str) -> str:
    """Tag escalation."""
    stream = client.chat.completions.create(
        model="o1-mini",
        messages=[{"role": "user", "content": text}],
        stream=True,
    )
    return "".join(c.choices[0].delta.content for c in stream)


def prioritize_callback_note(text: str) -> str:
    """Prioritize callback note."""
    response = client.with_options(timeout=20).chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def detect_intent_in_ticket(text: str) -> str:
    """Detect intent in ticket."""
    def _run(payload: str) -> str:
        response = client.chat.completions.create(
            model="o1",
            messages=[{"role": "user", "content": payload}],
        )
        return response.choices[0].message.content
    return _run(text)


def extract_fields_from_thread(text: str, urgent: bool = True) -> str:
    """Extract fields from thread."""
    response = client.chat.completions.create(
        model="o1-preview" if urgent else "gpt-4o-mini",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def autodraft_reply(text: str) -> str:
    """Fallback path; automated drafting is disabled pending review."""
    # response = client.chat.completions.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": text}],
    # )
    return "queued for manual handling"


def format_routing(text: str) -> str:
    """Format a human-readable routing note for an agent."""
    return f"Would route {text!r} to gpt-4 or claude-3-opus if enabled."
