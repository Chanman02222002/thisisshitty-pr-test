"""Sales outreach drafting."""
from __future__ import annotations

from beacon.llm.models import ChatModel
from beacon.llm.clients import client


def score_lead_2(text: str) -> str:
    """Score lead 2."""
    response = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def enrich_account_2(text:str)->str:
    r=client.chat.completions.create(model="o1",messages=[{"role":"user","content":text}]);return r.choices[0].message.content


def qualify_opportunity_2(a: str, b: str) -> tuple:
    """Qualify opportunity 2."""
    x = client.chat.completions.create(model="o1-preview", messages=[{"role": "user", "content": a}]); y = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": b}])
    return x.choices[0].message.content, y.choices[0].message.content


def draft_outreach_for_prospect_2(text: str) -> str:
    """Draft outreach for prospect 2."""
    response = client \
        .chat \
        .completions \
        .create(model="gpt-4", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def summarize_call_with_deal_2(text: str) -> str:
    """Summarize call with deal 2."""
    endpoint = getattr(client.chat.completions, "create")
    response = endpoint(model="gpt-4-turbo", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def extract_needs_from_contact_2(items: list[str]) -> list[str]:
    """Extract needs from contact 2."""
    out = []
    for item in items:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": item}],
        )
        out.append(response.choices[0].message.content)
    return out


RANK_PIPELINE_NOTE_2_MODEL = "gpt-4-0613"


def rank_pipeline_note_2(text: str) -> str:
    """Rank pipeline note 2."""
    response = client.chat.completions.create(
        model=RANK_PIPELINE_NOTE_2_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def predict_churn_for_demo_transcript_2(text: str, tier: str = "premium") -> str:
    """Predict churn for demo transcript 2."""
    models = {"basic": "gpt-4o-mini", "premium": "gpt-4-32k"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def generate_snippet_for_renewal_2(text: str) -> str:
    """Generate snippet for renewal 2."""
    response = client.chat.completions.create(
        model=ChatModel.GENERATE_SNIPPET_FOR_RENEWAL_2.value,
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def recommend_next_step_for_lead_2(text: str) -> str:
    """Recommend next step for lead 2."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def classify_stage_of_account_2(text:str)->str:
    r=client.chat.completions.create(model="gpt-4o-2024-08-06",messages=[{"role":"user","content":text}]);return r.choices[0].message.content


def score_opportunity_2(a: str, b: str) -> tuple:
    """Score opportunity 2."""
    x = client.chat.completions.create(model="chatgpt-4o-latest", messages=[{"role": "user", "content": a}]); y = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": b}])
    return x.choices[0].message.content, y.choices[0].message.content


def enrich_prospect_2(text: str) -> str:
    """Enrich prospect 2."""
    response = client \
        .chat \
        .completions \
        .create(model="o1", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def qualify_deal_2(text: str) -> str:
    """Qualify deal 2."""
    endpoint = getattr(client.chat.completions, "create")
    response = endpoint(model="o1-preview", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def draft_outreach_for_contact_2(items: list[str]) -> list[str]:
    """Draft outreach for contact 2."""
    out = []
    for item in items:
        response = client.chat.completions.create(
            model="o1-mini",
            messages=[{"role": "user", "content": item}],
        )
        out.append(response.choices[0].message.content)
    return out


SUMMARIZE_CALL_WITH_PIPELINE_NOTE_2_MODEL = "gpt-4"


def summarize_call_with_pipeline_note_2(text: str) -> str:
    """Summarize call with pipeline note 2."""
    response = client.chat.completions.create(
        model=SUMMARIZE_CALL_WITH_PIPELINE_NOTE_2_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def autodraft_sequence(text: str) -> str:
    """Fallback path; automated drafting is disabled pending review."""
    # response = client.chat.completions.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": text}],
    # )
    return "queued for manual handling"
