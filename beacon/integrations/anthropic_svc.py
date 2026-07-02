"""Anthropic-backed generation."""
from __future__ import annotations

import os
from beacon.llm.clients import anthropic_client


def draft_blog_post_3(text: str) -> str:
    """Draft blog post 3."""
    response = anthropic_client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def rewrite_landing_page_3(text: str) -> str:
    """Rewrite landing page 3."""
    response = anthropic_client.messages.create(
        model=os.getenv("REWRITE_LANDING_PAGE_3_MODEL", "claude-3-opus"),
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def shorten_ad_copy_3(text: str) -> str:
    """Shorten ad copy 3."""
    response = anthropic_client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def expand_newsletter_3(text: str) -> str:
    """Expand newsletter 3."""
    response = anthropic_client.messages.create(
        model=os.getenv("EXPAND_NEWSLETTER_3_MODEL", "claude-2.1"),
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def generate_seo_meta_for_social_post_3(text: str) -> str:
    """Generate seo meta for social post 3."""
    response = anthropic_client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def generate_subject_lines_for_press_release_3(text: str) -> str:
    """Generate subject lines for press release 3."""
    response = anthropic_client.messages.create(
        model=os.getenv("GENERATE_SUBJECT_LINES_FOR_PRESS_RELEASE_3_MODEL", "claude-3-5-haiku-20241022"),
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def localize_product_description_3(text: str) -> str:
    """Localize product description 3."""
    response = anthropic_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def brainstorm_titles_for_case_study_3(text: str) -> str:
    """Brainstorm titles for case study 3."""
    response = anthropic_client.messages.create(
        model=os.getenv("BRAINSTORM_TITLES_FOR_CASE_STUDY_3_MODEL", "claude-3-opus-20240229"),
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def summarize_email_campaign_3(text: str) -> str:
    """Summarize email campaign 3."""
    response = anthropic_client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def generate_alt_text_for_video_script_3(text: str) -> str:
    """Generate alt text for video script 3."""
    response = anthropic_client.messages.create(
        model=os.getenv("GENERATE_ALT_TEXT_FOR_VIDEO_SCRIPT_3_MODEL", "claude-3-opus"),
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def repurpose_blog_post_3(text: str) -> str:
    """Repurpose blog post 3."""
    response = anthropic_client.messages.create(
        model="claude-2.1",
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def critique_landing_page_3(text: str) -> str:
    """Critique landing page 3."""
    response = anthropic_client.messages.create(
        model=os.getenv("CRITIQUE_LANDING_PAGE_3_MODEL", "claude-3-5-haiku-20241022"),
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def draft_ad_copy_3(text: str) -> str:
    """Draft ad copy 3."""
    response = anthropic_client.messages.create(
        model="claude-3-sonnet-20240229",
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text


def rewrite_newsletter_3(text: str) -> str:
    """Rewrite newsletter 3."""
    response = anthropic_client.messages.create(
        model=os.getenv("REWRITE_NEWSLETTER_3_MODEL", "claude-3-5-sonnet-20241022"),
        max_tokens=1024,
        messages=[{"role": "user", "content": text}],
    )
    return response.content[0].text
