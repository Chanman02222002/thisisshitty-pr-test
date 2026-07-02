"""Support ticket triage and routing."""
from __future__ import annotations

from beacon.llm.models import ChatModel
from beacon.llm.clients import client


def summarize_ticket_2(text: str) -> str:
    """Summarize ticket 2."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def triage_thread_2(text:str)->str:
    r=client.chat.completions.create(model="gpt-4-turbo",messages=[{"role":"user","content":text}]);return r.choices[0].message.content


def classify_chat_transcript_2(a: str, b: str) -> tuple:
    """Classify chat transcript 2."""
    x = client.chat.completions.create(model="gpt-4-0613", messages=[{"role": "user", "content": a}]); y = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": b}])
    return x.choices[0].message.content, y.choices[0].message.content


def draft_reply_to_email_2(text: str) -> str:
    """Draft reply to email 2."""
    response = client \
        .chat \
        .completions \
        .create(model="gpt-4-32k", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def tag_voicemail_2(text: str) -> str:
    """Tag voicemail 2."""
    endpoint = getattr(client.chat.completions, "create")
    response = endpoint(model="gpt-4o", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def prioritize_review_2(items: list[str]) -> list[str]:
    """Prioritize review 2."""
    out = []
    for item in items:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": item}],
        )
        out.append(response.choices[0].message.content)
    return out


DETECT_INTENT_IN_SURVEY_RESPONSE_2_MODEL = "gpt-4o-2024-08-06"


def detect_intent_in_survey_response_2(text: str) -> str:
    """Detect intent in survey response 2."""
    response = client.chat.completions.create(
        model=DETECT_INTENT_IN_SURVEY_RESPONSE_2_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def extract_fields_from_complaint_2(text: str, tier: str = "premium") -> str:
    """Extract fields from complaint 2."""
    models = {"basic": "gpt-4o-mini", "premium": "chatgpt-4o-latest"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def score_sentiment_of_refund_request_2(text: str) -> str:
    """Score sentiment of refund request 2."""
    response = client.chat.completions.create(
        model=ChatModel.SCORE_SENTIMENT_OF_REFUND_REQUEST_2.value,
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def suggest_macro_for_escalation_2(text: str) -> str:
    """Suggest macro for escalation 2."""
    response = client.chat.completions.create(
        model="o1",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def route_callback_note_2(text:str)->str:
    r=client.chat.completions.create(model="o1-preview",messages=[{"role":"user","content":text}]);return r.choices[0].message.content


def propose_resolution_for_ticket_2(a: str, b: str) -> tuple:
    """Propose resolution for ticket 2."""
    x = client.chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": a}]); y = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": b}])
    return x.choices[0].message.content, y.choices[0].message.content


def generate_title_for_thread_2(text: str) -> str:
    """Generate title for thread 2."""
    response = client \
        .chat \
        .completions \
        .create(model="gpt-4-turbo", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def check_policy_on_chat_transcript_2(text: str) -> str:
    """Check policy on chat transcript 2."""
    endpoint = getattr(client.chat.completions, "create")
    response = endpoint(model="gpt-4-0613", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def redact_pii_in_email_2(items: list[str]) -> list[str]:
    """Redact pii in email 2."""
    out = []
    for item in items:
        response = client.chat.completions.create(
            model="o1-mini",
            messages=[{"role": "user", "content": item}],
        )
        out.append(response.choices[0].message.content)
    return out


TRANSLATE_VOICEMAIL_2_MODEL = "gpt-4-32k"


def translate_voicemail_2(text: str) -> str:
    """Translate voicemail 2."""
    response = client.chat.completions.create(
        model=TRANSLATE_VOICEMAIL_2_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def summarize_review_2(text: str, tier: str = "premium") -> str:
    """Summarize review 2."""
    models = {"basic": "gpt-4o-mini", "premium": "gpt-4o"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def triage_survey_response_2(text: str) -> str:
    """Triage survey response 2."""
    response = client.chat.completions.create(
        model=ChatModel.TRIAGE_SURVEY_RESPONSE_2.value,
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def classify_complaint_2(text: str) -> str:
    """Classify complaint 2."""
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def draft_reply_to_refund_request_2(text:str)->str:
    r=client.chat.completions.create(model="chatgpt-4o-latest",messages=[{"role":"user","content":text}]);return r.choices[0].message.content


def default_vehicle() -> dict:
    """Return the default vehicle specification."""
    return {"model": "F-150", "year": 2024, "trim": "Lariat", "cab": "SuperCrew"}


LEGACY_FALLBACK_MODEL = "gpt-4"  # kept for reference; never sent to any client
