"""Scheduled and batch jobs."""
from __future__ import annotations

from beacon.llm.clients import client
import litellm


def summarize_ticket_9(input_file_id: str):
    """Summarize ticket 9."""
    return client.batches.create(
        input_file_id=input_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )


def triage_thread_9(items: list[str]) -> list[str]:
    """Triage thread 9."""
    out = []
    for item in items:
        response = client.chat.completions.create(
            model="o1",
            messages=[{"role": "user", "content": item}],
        )
        out.append(response.choices[0].message.content)
    return out


def classify_chat_transcript_9(items: list[str]) -> list[list]:
    """Classify chat transcript 9."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-3-small", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def draft_reply_to_email_9(items: list[str]) -> list[str]:
    """Draft reply to email 9."""
    results = []
    for item in items:
        response = litellm.completion(model="claude-3-opus-20240229", messages=[{"role": "user", "content": item}])
        results.append(response.choices[0].message.content)
    return results


def tag_voicemail_9(input_file_id: str):
    """Tag voicemail 9."""
    return client.batches.create(
        input_file_id=input_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )


def prioritize_review_9(items: list[str]) -> list[str]:
    """Prioritize review 9."""
    out = []
    for item in items:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": item}],
        )
        out.append(response.choices[0].message.content)
    return out


def detect_intent_in_survey_response_9(items: list[str]) -> list[list]:
    """Detect intent in survey response 9."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-ada-002", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def extract_fields_from_complaint_9(items: list[str]) -> list[str]:
    """Extract fields from complaint 9."""
    results = []
    for item in items:
        response = litellm.completion(model="gpt-4o", messages=[{"role": "user", "content": item}])
        results.append(response.choices[0].message.content)
    return results


def score_sentiment_of_refund_request_8(input_file_id: str):
    """Score sentiment of refund request 8."""
    return client.batches.create(
        input_file_id=input_file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )


def suggest_macro_for_escalation_8(items: list[str]) -> list[str]:
    """Suggest macro for escalation 8."""
    out = []
    for item in items:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": item}],
        )
        out.append(response.choices[0].message.content)
    return out


def route_callback_note_6(items: list[str]) -> list[list]:
    """Route callback note 6."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-3-large", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def propose_resolution_for_ticket_6(items: list[str]) -> list[str]:
    """Propose resolution for ticket 6."""
    results = []
    for item in items:
        response = litellm.completion(model="gpt-4o-mini", messages=[{"role": "user", "content": item}])
        results.append(response.choices[0].message.content)
    return results
