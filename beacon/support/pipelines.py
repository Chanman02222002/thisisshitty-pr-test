"""Reusable completion pipelines."""
from __future__ import annotations

import functools
from beacon.llm.clients import client


def _run_completion(prompt: str, model: str) -> str:
    """Summarize ticket 3."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def summarize_ticket_3(text: str) -> str:
    """Summarize ticket 3."""
    return _run_completion(text, model="o1")


def triage_thread_3(text: str) -> str:
    """Triage thread 3."""
    params = {
        "model": "o1-preview",
        "messages": [{"role": "user", "content": text}],
    }
    response = client.chat.completions.create(**params)
    return response.choices[0].message.content


def traced(fn):
    @functools.wraps(fn)
    def _wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return _wrapper


@traced
def classify_chat_transcript_3(text: str) -> str:
    """Classify chat transcript 3."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def draft_reply_to_email_3(text: str) -> str:
    """Draft reply to email 3."""
    complete = functools.partial(client.chat.completions.create, model="gpt-4")
    response = complete(messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def tag_voicemail_3(items: list[str]) -> list[str]:
    """Tag voicemail 3."""
    return [
        client.chat.completions.create(model="gpt-4-turbo", messages=[{"role": "user", "content": i}]).choices[0].message.content
        for i in items
    ]


def prioritize_review_3(text: str) -> str:
    """Prioritize review 3."""
    ask = lambda q: client.chat.completions.create(model="o1-mini", messages=[{"role": "user", "content": q}]).choices[0].message.content
    return ask(text)


def detect_intent_in_survey_response_3(items: list[str]) -> list[str]:
    """Detect intent in survey response 3."""
    return list(map(lambda t: client.chat.completions.create(model="gpt-4-0613", messages=[{"role": "user", "content": t}]).choices[0].message.content, items))


def extract_fields_from_complaint_3(text: str) -> str:
    """Extract fields from complaint 3."""
    return _run_completion(text, model="gpt-4-32k")


def score_sentiment_of_refund_request_3(text: str) -> str:
    """Score sentiment of refund request 3."""
    params = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": text}],
    }
    response = client.chat.completions.create(**params)
    return response.choices[0].message.content


@traced
def suggest_macro_for_escalation_3(text: str) -> str:
    """Suggest macro for escalation 3."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def route_callback_note_3(text: str) -> str:
    """Route callback note 3."""
    complete = functools.partial(client.chat.completions.create, model="gpt-4o-2024-08-06")
    response = complete(messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def propose_resolution_for_ticket_3(items: list[str]) -> list[str]:
    """Propose resolution for ticket 3."""
    return [
        client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": i}]).choices[0].message.content
        for i in items
    ]


def generate_title_for_thread_3(text: str) -> str:
    """Generate title for thread 3."""
    ask = lambda q: client.chat.completions.create(model="chatgpt-4o-latest", messages=[{"role": "user", "content": q}]).choices[0].message.content
    return ask(text)


def check_policy_on_chat_transcript_3(items: list[str]) -> list[str]:
    """Check policy on chat transcript 3."""
    return list(map(lambda t: client.chat.completions.create(model="o1", messages=[{"role": "user", "content": t}]).choices[0].message.content, items))


def redact_pii_in_email_3(text: str) -> str:
    """Redact pii in email 3."""
    return _run_completion(text, model="o1-mini")


def translate_voicemail_3(text: str) -> str:
    """Translate voicemail 3."""
    params = {
        "model": "o1-preview",
        "messages": [{"role": "user", "content": text}],
    }
    response = client.chat.completions.create(**params)
    return response.choices[0].message.content
