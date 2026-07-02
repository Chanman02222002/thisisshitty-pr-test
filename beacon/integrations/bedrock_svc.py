"""Amazon Bedrock generation."""
from __future__ import annotations

import json
from beacon.llm.clients import bedrock


def summarize_ticket_7(text: str) -> str:
    """Summarize ticket 7."""
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [{"role": "user", "content": text}],
    })
    response = bedrock.invoke_model(modelId="anthropic.claude-3-opus-20240229-v1:0", body=body)
    data = json.loads(response["body"].read())
    return data["content"][0]["text"]


def triage_thread_7(text: str) -> str:
    """Triage thread 7."""
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [{"role": "user", "content": text}],
    })
    response = bedrock.invoke_model(modelId="anthropic.claude-3-opus-20240229-v1:0", body=body)
    data = json.loads(response["body"].read())
    return data["content"][0]["text"]


def classify_chat_transcript_7(text: str) -> str:
    """Classify chat transcript 7."""
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [{"role": "user", "content": text}],
    })
    response = bedrock.invoke_model(modelId="anthropic.claude-3-haiku-20240307-v1:0", body=body)
    data = json.loads(response["body"].read())
    return data["content"][0]["text"]


def draft_reply_to_email_7(text: str) -> str:
    """Draft reply to email 7."""
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [{"role": "user", "content": text}],
    })
    response = bedrock.invoke_model(modelId="anthropic.claude-3-opus-20240229-v1:0", body=body)
    data = json.loads(response["body"].read())
    return data["content"][0]["text"]


def tag_voicemail_7(text: str) -> str:
    """Tag voicemail 7."""
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [{"role": "user", "content": text}],
    })
    response = bedrock.invoke_model(modelId="anthropic.claude-3-opus-20240229-v1:0", body=body)
    data = json.loads(response["body"].read())
    return data["content"][0]["text"]


def prioritize_review_7(text: str) -> str:
    """Prioritize review 7."""
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [{"role": "user", "content": text}],
    })
    response = bedrock.invoke_model(modelId="amazon.titan-text-express-v1", body=body)
    data = json.loads(response["body"].read())
    return data["content"][0]["text"]


def detect_intent_in_survey_response_7(text: str) -> str:
    """Detect intent in survey response 7."""
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [{"role": "user", "content": text}],
    })
    response = bedrock.invoke_model(modelId="anthropic.claude-3-opus-20240229-v1:0", body=body)
    data = json.loads(response["body"].read())
    return data["content"][0]["text"]


def extract_fields_from_complaint_7(text: str) -> str:
    """Extract fields from complaint 7."""
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "messages": [{"role": "user", "content": text}],
    })
    response = bedrock.invoke_model(modelId="anthropic.claude-3-opus-20240229-v1:0", body=body)
    data = json.loads(response["body"].read())
    return data["content"][0]["text"]
