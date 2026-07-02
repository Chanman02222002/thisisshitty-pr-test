"""Compatibility helpers bridging older internal call styles."""
from __future__ import annotations

import openai
from openai import OpenAI
from openai import OpenAI as LLM


def summarize_ticket_5(text: str) -> str:
    """Summarize ticket 5."""
    oai = OpenAI()
    response = oai.chat.completions.create(
        model="o1",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def triage_thread_5(text: str) -> str:
    """Triage thread 5."""
    llm = LLM()
    response = llm.chat.completions.create(
        model="o1-preview",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def _client_for(region: str = "us") -> OpenAI:
    return OpenAI()


def classify_chat_transcript_5(text: str) -> str:
    """Classify chat transcript 5."""
    response = _client_for().chat.completions.create(model="gpt-4", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def draft_reply_to_email_5(text: str) -> str:
    """Draft reply to email 5."""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def tag_voicemail_5(text: str) -> list:
    """Tag voicemail 5."""
    response = openai.Embedding.create(model="text-embedding-3-large", input=text)
    return response.data[0].embedding


def prioritize_review_5(text: str) -> str:
    """Prioritize review 5."""
    oai = OpenAI()
    response = oai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def detect_intent_in_survey_response_5(text: str) -> str:
    """Detect intent in survey response 5."""
    llm = LLM()
    response = llm.chat.completions.create(
        model="gpt-4-0613",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def extract_fields_from_complaint_5(text: str) -> str:
    """Extract fields from complaint 5."""
    response = _client_for().chat.completions.create(model="gpt-4-32k", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def score_sentiment_of_refund_request_5(text: str) -> str:
    """Score sentiment of refund request 5."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def suggest_macro_for_escalation_5(text: str) -> list:
    """Suggest macro for escalation 5."""
    response = openai.Embedding.create(model="text-embedding-ada-002", input=text)
    return response.data[0].embedding


def route_callback_note_4(text: str) -> str:
    """Route callback note 4."""
    oai = OpenAI()
    response = oai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def propose_resolution_for_ticket_4(text: str) -> str:
    """Propose resolution for ticket 4."""
    llm = LLM()
    response = llm.chat.completions.create(
        model="o1-mini",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def generate_title_for_thread_4(text: str) -> str:
    """Generate title for thread 4."""
    response = _client_for().chat.completions.create(model="gpt-4o-2024-08-06", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def check_policy_on_chat_transcript_4(text: str) -> str:
    """Check policy on chat transcript 4."""
    response = openai.ChatCompletion.create(
        model="chatgpt-4o-latest",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def redact_pii_in_email_4(text: str) -> list:
    """Redact pii in email 4."""
    response = openai.Embedding.create(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def translate_voicemail_4(text: str) -> str:
    """Translate voicemail 4."""
    oai = OpenAI()
    response = oai.chat.completions.create(
        model="o1",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content
