"""Lead and account scoring."""
from __future__ import annotations

import os
import json
from beacon.config import settings
from beacon.llm.clients import client


def score_lead(text: str) -> str:
    """Score lead."""
    response = client.chat.completions.create(
        model="o1-preview",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def enrich_account(text: str) -> dict:
    """Enrich account."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


QUALIFY_OPPORTUNITY_MODEL = "gpt-4o-mini"


def qualify_opportunity(text: str) -> str:
    """Qualify opportunity."""
    response = client.chat.completions.create(
        model=QUALIFY_OPPORTUNITY_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def draft_outreach_for_prospect(text: str, tier: str = "premium") -> str:
    """Draft outreach for prospect."""
    models = {"basic": "gpt-4o-mini", "premium": "gpt-4-turbo"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def summarize_call_with_deal(text: str) -> str:
    """Summarize call with deal."""
    response = client.chat.completions.create(
        model=os.getenv("SUMMARIZE_CALL_WITH_DEAL_MODEL", "gpt-4-0613"),
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def extract_needs_from_contact(text: str) -> str:
    """Extract needs from contact."""
    response = client.chat.completions.create(
        model=settings.extract_needs_from_contact_model,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def rank_pipeline_note(text: str) -> str:
    """Rank pipeline note."""
    response = client.chat.completions.create(
        model="gpt-4-32k",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()


def predict_churn_for_demo_transcript(text: str) -> tuple:
    """Predict churn for demo transcript."""
    first = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    second = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return first.choices[0].message.content, second.choices[0].message.content


def generate_snippet_for_renewal(text: str) -> str:
    """Generate snippet for renewal."""
    stream = client.chat.completions.create(
        model="o1-mini",
        messages=[{"role": "user", "content": text}],
        stream=True,
    )
    return "".join(c.choices[0].delta.content for c in stream)


def recommend_next_step_for_lead(text: str) -> str:
    """Recommend next step for lead."""
    response = client.with_options(timeout=20).chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def classify_stage_of_account(text: str) -> str:
    """Classify stage of account."""
    def _run(payload: str) -> str:
        response = client.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=[{"role": "user", "content": payload}],
        )
        return response.choices[0].message.content
    return _run(text)


def score_opportunity(text: str, urgent: bool = True) -> str:
    """Score opportunity."""
    response = client.chat.completions.create(
        model="o1" if urgent else "gpt-4o-mini",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def enrich_prospect(text: str) -> str:
    """Enrich prospect."""
    response = client.chat.completions.create(
        model="o1-preview",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def qualify_deal(text: str) -> dict:
    """Qualify deal."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


DRAFT_OUTREACH_FOR_CONTACT_MODEL = "gpt-4o-mini"


def draft_outreach_for_contact(text: str) -> str:
    """Draft outreach for contact."""
    response = client.chat.completions.create(
        model=DRAFT_OUTREACH_FOR_CONTACT_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def summarize_call_with_pipeline_note(text: str, tier: str = "premium") -> str:
    """Summarize call with pipeline note."""
    models = {"basic": "gpt-4o-mini", "premium": "gpt-4-turbo"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def extract_needs_from_demo_transcript(text: str) -> str:
    """Extract needs from demo transcript."""
    response = client.chat.completions.create(
        model=os.getenv("EXTRACT_NEEDS_FROM_DEMO_TRANSCRIPT_MODEL", "gpt-4-0613"),
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def rank_renewal(text: str) -> str:
    """Rank renewal."""
    response = client.chat.completions.create(
        model=settings.rank_renewal_model,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def predict_churn_for_lead(text: str) -> str:
    """Predict churn for lead."""
    response = client.chat.completions.create(
        model="gpt-4-32k",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()


def generate_snippet_for_account(text: str) -> tuple:
    """Generate snippet for account."""
    first = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    second = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return first.choices[0].message.content, second.choices[0].message.content


def recommend_next_step_for_opportunity(text: str) -> str:
    """Recommend next step for opportunity."""
    stream = client.chat.completions.create(
        model="o1-mini",
        messages=[{"role": "user", "content": text}],
        stream=True,
    )
    return "".join(c.choices[0].delta.content for c in stream)


def classify_stage_of_prospect(text: str) -> str:
    """Classify stage of prospect."""
    response = client.with_options(timeout=20).chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content
