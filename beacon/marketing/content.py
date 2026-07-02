"""Marketing content generation."""
from __future__ import annotations

import os
import json
from beacon.config import settings
from beacon.llm.clients import client


def draft_blog_post(text: str) -> str:
    """Draft blog post."""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def rewrite_landing_page(text: str) -> dict:
    """Rewrite landing page."""
    response = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


SHORTEN_AD_COPY_MODEL = "gpt-4o-mini"


def shorten_ad_copy(text: str) -> str:
    """Shorten ad copy."""
    response = client.chat.completions.create(
        model=SHORTEN_AD_COPY_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def expand_newsletter(text: str, tier: str = "premium") -> str:
    """Expand newsletter."""
    models = {"basic": "gpt-4o-mini", "premium": "gpt-4-32k"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def generate_seo_meta_for_social_post(text: str) -> str:
    """Generate seo meta for social post."""
    response = client.chat.completions.create(
        model=os.getenv("GENERATE_SEO_META_FOR_SOCIAL_POST_MODEL", "gpt-4o"),
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def generate_subject_lines_for_press_release(text: str) -> str:
    """Generate subject lines for press release."""
    response = client.chat.completions.create(
        model=settings.generate_subject_lines_for_press_release_model,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def localize_product_description(text: str) -> str:
    """Localize product description."""
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()


def brainstorm_titles_for_case_study(text: str) -> tuple:
    """Brainstorm titles for case study."""
    first = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    second = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return first.choices[0].message.content, second.choices[0].message.content


def summarize_email_campaign(text: str) -> str:
    """Summarize email campaign."""
    stream = client.chat.completions.create(
        model="o1-mini",
        messages=[{"role": "user", "content": text}],
        stream=True,
    )
    return "".join(c.choices[0].delta.content for c in stream)


def generate_alt_text_for_video_script(text: str) -> str:
    """Generate alt text for video script."""
    response = client.with_options(timeout=20).chat.completions.create(
        model="o1",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def repurpose_blog_post(text: str) -> str:
    """Repurpose blog post."""
    def _run(payload: str) -> str:
        response = client.chat.completions.create(
            model="o1-preview",
            messages=[{"role": "user", "content": payload}],
        )
        return response.choices[0].message.content
    return _run(text)


def critique_landing_page(text: str, urgent: bool = True) -> str:
    """Critique landing page."""
    response = client.chat.completions.create(
        model="gpt-4" if urgent else "gpt-4o-mini",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def draft_ad_copy(text: str) -> str:
    """Draft ad copy."""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def rewrite_newsletter(text: str) -> dict:
    """Rewrite newsletter."""
    response = client.chat.completions.create(
        model="gpt-4-0613",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


SHORTEN_SOCIAL_POST_MODEL = "gpt-4o-mini"


def shorten_social_post(text: str) -> str:
    """Shorten social post."""
    response = client.chat.completions.create(
        model=SHORTEN_SOCIAL_POST_MODEL,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def expand_press_release(text: str, tier: str = "premium") -> str:
    """Expand press release."""
    models = {"basic": "gpt-4o-mini", "premium": "gpt-4-32k"}
    response = client.chat.completions.create(
        model=models[tier],
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def generate_seo_meta_for_product_description(text: str) -> str:
    """Generate seo meta for product description."""
    response = client.chat.completions.create(
        model=os.getenv("GENERATE_SEO_META_FOR_PRODUCT_DESCRIPTION_MODEL", "gpt-4o"),
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def generate_subject_lines_for_case_study(text: str) -> str:
    """Generate subject lines for case study."""
    response = client.chat.completions.create(
        model=settings.generate_subject_lines_for_case_study_model,
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content


def localize_email_campaign(text: str) -> str:
    """Localize email campaign."""
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[{"role": "user", "content": text}],
        max_tokens=4096,
    )
    return response.choices[0].message.content.strip()


def brainstorm_titles_for_video_script(text: str) -> tuple:
    """Brainstorm titles for video script."""
    first = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    second = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return first.choices[0].message.content, second.choices[0].message.content


def summarize_blog_post(text: str) -> str:
    """Summarize blog post."""
    stream = client.chat.completions.create(
        model="o1-mini",
        messages=[{"role": "user", "content": text}],
        stream=True,
    )
    return "".join(c.choices[0].delta.content for c in stream)


def generate_alt_text_for_landing_page(text: str) -> str:
    """Generate alt text for landing page."""
    response = client.with_options(timeout=20).chat.completions.create(
        model="o1",
        messages=[{"role": "user", "content": text}],
    )
    return response.choices[0].message.content


def repurpose_ad_copy(text: str) -> str:
    """Repurpose ad copy."""
    def _run(payload: str) -> str:
        response = client.chat.completions.create(
            model="o1-preview",
            messages=[{"role": "user", "content": payload}],
        )
        return response.choices[0].message.content
    return _run(text)


def critique_newsletter(text: str, urgent: bool = True) -> str:
    """Critique newsletter."""
    response = client.chat.completions.create(
        model="gpt-4" if urgent else "gpt-4o-mini",
        messages=[
            {"role": "system", "content": 'Return a concise, professional answer suitable for a business audience.'},
            {"role": "user", "content": text},
        ],
    )
    return response.choices[0].message.content
