"""integrations.py - non-OpenAI provider call sites.

The scanner should recognise model calls across providers and wrapper
libraries, not just `client.chat.completions.create`. Each IN* function is one
real call the scanner MUST find. All run against the offline mock in fake_ai.py.
"""
from __future__ import annotations

from typing import Any

# Imported under their real-world names so the call sites read naturally.
import fake_ai as openai          # legacy module-style access lives here too
from fake_ai import Anthropic, ChatOpenAI, genai, litellm

anthropic_client = Anthropic(api_key="unused")
genai.configure(api_key="unused")


# IN01 -------------------------------------------------------------------------
def in01_anthropic_messages(note: str) -> str:
    """TRUE: Anthropic messages API, claude-3-opus."""
    response = anthropic_client.messages.create(
        model="claude-3-opus",
        max_tokens=256,
        messages=[{"role": "user", "content": note}],
    )
    return response.content[0].text


# IN02 -------------------------------------------------------------------------
def in02_google_gemini(note: str) -> str:
    """TRUE: Google Gemini, model name passed to GenerativeModel()."""
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(note)
    return response.text


# IN03 -------------------------------------------------------------------------
def in03_litellm_completion(note: str) -> str:
    """TRUE: litellm.completion with a model= kwarg."""
    response = litellm.completion(
        model="gpt-4o",
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# IN04 -------------------------------------------------------------------------
def in04_langchain_invoke(note: str) -> str:
    """TRUE: LangChain ChatOpenAI, model set on the constructor."""
    chat = ChatOpenAI(model="gpt-4o", temperature=0)
    response = chat.invoke(note)
    return response.content[0].text


# IN05 -------------------------------------------------------------------------
def in05_litellm_embedding(text: str) -> list[float]:
    """TRUE: litellm.embedding call."""
    response = litellm.embedding(model="text-embedding-3-small", input=text)
    return list(response.data[0].embedding)


# IN06 -------------------------------------------------------------------------
def in06_legacy_module_call(note: str) -> str:
    """TRUE: legacy module-style openai.ChatCompletion.create."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


def run_integrations() -> dict[str, Any]:
    return {
        "in01": in01_anthropic_messages("question"),
        "in02": in02_google_gemini("question"),
        "in03": in03_litellm_completion("question"),
        "in04": in04_langchain_invoke("question"),
        "in05": in05_litellm_embedding("question"),
        "in06": in06_legacy_module_call("question"),
    }
