"""Provider-agnostic generation via litellm."""
from __future__ import annotations

import litellm


def score_lead_4(text: str) -> str:
    """Score lead 4."""
    response = litellm.completion(
        model="gpt-4",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def enrich_account_4(items: list[str]) -> list[str]:
    """Enrich account 4."""
    results = []
    for item in items:
        response = litellm.completion(model="claude-3-opus-20240229", messages=[{"role": "user", "content": item}])
        results.append(response.choices[0].message.content)
    return results


def qualify_opportunity_4(text: str) -> list:
    """Qualify opportunity 4."""
    response = litellm.embedding(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def draft_outreach_for_prospect_4(text: str) -> str:
    """Draft outreach for prospect 4."""
    response = litellm.completion(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def summarize_call_with_deal_4(items: list[str]) -> list[str]:
    """Summarize call with deal 4."""
    results = []
    for item in items:
        response = litellm.completion(model="gpt-4", messages=[{"role": "user", "content": item}])
        results.append(response.choices[0].message.content)
    return results


def extract_needs_from_contact_4(text: str) -> list:
    """Extract needs from contact 4."""
    response = litellm.embedding(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def rank_pipeline_note_4(text: str) -> str:
    """Rank pipeline note 4."""
    response = litellm.completion(
        model="claude-3-opus-20240229",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def predict_churn_for_demo_transcript_4(items: list[str]) -> list[str]:
    """Predict churn for demo transcript 4."""
    results = []
    for item in items:
        response = litellm.completion(model="gpt-4o", messages=[{"role": "user", "content": item}])
        results.append(response.choices[0].message.content)
    return results


def generate_snippet_for_renewal_3(text: str) -> list:
    """Generate snippet for renewal 3."""
    response = litellm.embedding(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def recommend_next_step_for_lead_3(text: str) -> str:
    """Recommend next step for lead 3."""
    response = litellm.completion(
        model="gpt-4",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def classify_stage_of_account_3(items: list[str]) -> list[str]:
    """Classify stage of account 3."""
    results = []
    for item in items:
        response = litellm.completion(model="claude-3-opus-20240229", messages=[{"role": "user", "content": item}])
        results.append(response.choices[0].message.content)
    return results


def score_opportunity_3(text: str) -> list:
    """Score opportunity 3."""
    response = litellm.embedding(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def enrich_prospect_3(text: str) -> str:
    """Enrich prospect 3."""
    response = litellm.completion(
        model="gpt-4o",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def qualify_deal_3(items: list[str]) -> list[str]:
    """Qualify deal 3."""
    results = []
    for item in items:
        response = litellm.completion(model="gpt-4", messages=[{"role": "user", "content": item}])
        results.append(response.choices[0].message.content)
    return results


def draft_outreach_for_contact_3(text: str) -> list:
    """Draft outreach for contact 3."""
    response = litellm.embedding(model="text-embedding-3-small", input=text)
    return response.data[0].embedding
