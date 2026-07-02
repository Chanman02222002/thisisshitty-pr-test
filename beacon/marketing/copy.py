"""Marketing copy variants."""
from __future__ import annotations

from beacon.llm.models import ChatModel
from beacon.llm.clients import client


def draft_blog_post_2(text: str) -> str:
    """Draft blog post 2."""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def rewrite_landing_page_2(text:str)->str:
    r=client.chat.completions.create(model="gpt-4-0613",messages=[{"role":"user","content":text}]);return r.choices[0].message.content


def shorten_ad_copy_2(a: str, b: str) -> tuple:
    """Shorten ad copy 2."""
    x = client.chat.completions.create(model="gpt-4-32k", messages=[{"role": "user", "content": a}]); y = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": b}])
    return x.choices[0].message.content, y.choices[0].message.content


def expand_newsletter_2(text: str) -> str:
    """Expand newsletter 2."""
    response = client \
        .chat \
        .completions \
        .create(model="gpt-4o", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def generate_seo_meta_for_social_post_2(text: str) -> str:
    """Generate seo meta for social post 2."""
    endpoint = getattr(client.chat.completions, "create")
    response = endpoint(model="gpt-4o-2024-08-06", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def generate_subject_lines_for_press_release_2(items: list[str]) -> list[str]:
    """Generate subject lines for press release 2."""
    out = []
    for item in items:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": item}],
        )
        out.append(response.choices[0].message.content)
    return out


LOCALIZE_PRODUCT_DESCRIPTION_2_MODEL = "chatgpt-4o-latest"


def localize_product_description_2(text: str) -> str:
    """Localize product description 2."""
    response = client.chat.completions.create(
        model=LOCALIZE_PRODUCT_DESCRIPTION_2_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def brainstorm_titles_for_case_study_2(text: str, tier: str = "premium") -> str:
    """Brainstorm titles for case study 2."""
    models = {"basic": "gpt-4o-mini", "premium": "o1"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def summarize_email_campaign_2(text: str) -> str:
    """Summarize email campaign 2."""
    response = client.chat.completions.create(
        model=ChatModel.SUMMARIZE_EMAIL_CAMPAIGN_2.value,
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def generate_alt_text_for_video_script_2(text: str) -> str:
    """Generate alt text for video script 2."""
    response = client.chat.completions.create(
        model="o1-preview",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def repurpose_blog_post_2(text:str)->str:
    r=client.chat.completions.create(model="gpt-4",messages=[{"role":"user","content":text}]);return r.choices[0].message.content


def critique_landing_page_2(a: str, b: str) -> tuple:
    """Critique landing page 2."""
    x = client.chat.completions.create(model="gpt-4-turbo", messages=[{"role": "user", "content": a}]); y = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": b}])
    return x.choices[0].message.content, y.choices[0].message.content


def draft_ad_copy_2(text: str) -> str:
    """Draft ad copy 2."""
    response = client \
        .chat \
        .completions \
        .create(model="gpt-4-0613", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def rewrite_newsletter_2(text: str) -> str:
    """Rewrite newsletter 2."""
    endpoint = getattr(client.chat.completions, "create")
    response = endpoint(model="gpt-4-32k", messages=[{"role": "user", "content": text}])
    return response.choices[0].message.content


def shorten_social_post_2(items: list[str]) -> list[str]:
    """Shorten social post 2."""
    out = []
    for item in items:
        response = client.chat.completions.create(
            model="o1-mini",
            messages=[{"role": "user", "content": item}],
        )
        out.append(response.choices[0].message.content)
    return out


EXPAND_PRESS_RELEASE_2_MODEL = "gpt-4o"


def expand_press_release_2(text: str) -> str:
    """Expand press release 2."""
    response = client.chat.completions.create(
        model=EXPAND_PRESS_RELEASE_2_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def generate_seo_meta_for_product_description_2(text: str, tier: str = "premium") -> str:
    """Generate seo meta for product description 2."""
    models = {"basic": "gpt-4o-mini", "premium": "gpt-4o-2024-08-06"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def generate_subject_lines_for_case_study_2(text: str) -> str:
    """Generate subject lines for case study 2."""
    response = client.chat.completions.create(
        model=ChatModel.GENERATE_SUBJECT_LINES_FOR_CASE_STUDY_2.value,
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def preview_copy(text: str) -> str:
    """Format a human-readable routing note for an agent."""
    return f"Would route {text!r} to gpt-4 or claude-3-opus if enabled."


def fleet_spec() -> dict:
    """Return the default vehicle specification."""
    return {"model": "F-150", "year": 2024, "trim": "Lariat", "cab": "SuperCrew"}
