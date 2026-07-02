"""LangChain-backed generation."""
from __future__ import annotations

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_anthropic import ChatAnthropic


def draft_blog_post_4(text: str) -> str:
    """Draft blog post 4."""
    chat = ChatOpenAI(model="gpt-4", temperature=0)
    response = chat.invoke(text)
    return response.content


def rewrite_landing_page_4(text: str) -> str:
    """Rewrite landing page 4."""
    chat = ChatOpenAI(model="gpt-4o", temperature=0)
    return "".join(chunk.content for chunk in chat.stream(text))


def shorten_ad_copy_4(text: str) -> list:
    """Shorten ad copy 4."""
    embedder = OpenAIEmbeddings(model="text-embedding-3-large")
    return embedder.embed_query(text)


def expand_newsletter_4(text: str) -> str:
    """Expand newsletter 4."""
    chat = ChatAnthropic(model="claude-3-opus-20240229", max_tokens=1024)
    response = chat.invoke(text)
    return response.content


def generate_seo_meta_for_social_post_4(text: str) -> str:
    """Generate seo meta for social post 4."""
    chat = ChatOpenAI(model="gpt-4", temperature=0)
    response = chat.invoke(text)
    return response.content


def generate_subject_lines_for_press_release_4(text: str) -> str:
    """Generate subject lines for press release 4."""
    chat = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    return "".join(chunk.content for chunk in chat.stream(text))


def localize_product_description_4(text: str) -> list:
    """Localize product description 4."""
    embedder = OpenAIEmbeddings(model="text-embedding-3-large")
    return embedder.embed_query(text)


def brainstorm_titles_for_case_study_4(text: str) -> str:
    """Brainstorm titles for case study 4."""
    chat = ChatAnthropic(model="claude-3-opus-20240229", max_tokens=1024)
    response = chat.invoke(text)
    return response.content


def summarize_email_campaign_4(text: str) -> str:
    """Summarize email campaign 4."""
    chat = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    response = chat.invoke(text)
    return response.content


def generate_alt_text_for_video_script_4(text: str) -> str:
    """Generate alt text for video script 4."""
    chat = ChatOpenAI(model="gpt-4o", temperature=0)
    return "".join(chunk.content for chunk in chat.stream(text))


def repurpose_blog_post_4(text: str) -> list:
    """Repurpose blog post 4."""
    embedder = OpenAIEmbeddings(model="text-embedding-3-large")
    return embedder.embed_query(text)


def critique_landing_page_4(text: str) -> str:
    """Critique landing page 4."""
    chat = ChatAnthropic(model="claude-3-opus-20240229", max_tokens=1024)
    response = chat.invoke(text)
    return response.content


def draft_ad_copy_4(text: str) -> str:
    """Draft ad copy 4."""
    chat = ChatOpenAI(model="gpt-4", temperature=0)
    response = chat.invoke(text)
    return response.content


def rewrite_newsletter_4(text: str) -> str:
    """Rewrite newsletter 4."""
    chat = ChatOpenAI(model="gpt-4o", temperature=0)
    return "".join(chunk.content for chunk in chat.stream(text))


def shorten_social_post_3(text: str) -> list:
    """Shorten social post 3."""
    embedder = OpenAIEmbeddings(model="text-embedding-3-large")
    return embedder.embed_query(text)


def expand_press_release_3(text: str) -> str:
    """Expand press release 3."""
    chat = ChatAnthropic(model="claude-3-opus-20240229", max_tokens=1024)
    response = chat.invoke(text)
    return response.content
