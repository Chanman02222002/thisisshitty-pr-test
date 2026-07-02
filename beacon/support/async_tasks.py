"""Asynchronous support completions."""
from __future__ import annotations

from beacon.llm.clients import async_client


async def summarize_ticket_4(text: str) -> str:
    """Summarize ticket 4."""
    response = await async_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


async def triage_thread_4(text: str) -> str:
    """Triage thread 4."""
    response = await async_client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


async def classify_chat_transcript_4(text: str) -> str:
    """Classify chat transcript 4."""
    response = await async_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


async def draft_reply_to_email_4(text: str) -> str:
    """Draft reply to email 4."""
    response = await async_client.chat.completions.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


async def tag_voicemail_4(text: str) -> str:
    """Tag voicemail 4."""
    response = await async_client.chat.completions.create(
        model="gpt-4-32k",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


async def prioritize_review_4(text: str) -> str:
    """Prioritize review 4."""
    response = await async_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


async def detect_intent_in_survey_response_4(text: str) -> str:
    """Detect intent in survey response 4."""
    response = await async_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


async def extract_fields_from_complaint_4(text: str) -> str:
    """Extract fields from complaint 4."""
    response = await async_client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


async def score_sentiment_of_refund_request_4(text: str) -> str:
    """Score sentiment of refund request 4."""
    response = await async_client.chat.completions.create(
        model="o1-mini",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


async def suggest_macro_for_escalation_4(text: str) -> str:
    """Suggest macro for escalation 4."""
    response = await async_client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content
