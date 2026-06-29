"""Business-facing AI call sites (the 'primary' set).

These six functions are deliberately written the *plain*, easy-to-detect way:
a module-level `client`, a literal `model=` keyword, one call per function.
They are the baseline the scanner must always catch.

They are intentionally left UN-instrumented: there is no usage/cost tracker
wired in here. The scanner is expected to (re)apply the tracker. Models are set
to their expensive originals so the scanner has real savings to propose.
"""
from __future__ import annotations

import json
import os
from typing import Any

from fake_ai import client


def summarize_support_ticket(note: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Summarize the support note in one sentence."},
            {"role": "user", "content": note},
        ],
    )
    return response.choices[0].message.content


def classify_sales_lead(lead: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Classify this lead as Hot, Warm, or Cold."},
            {"role": "user", "content": lead},
        ],
    )
    return response.choices[0].message.content


def extract_contact_json(message: str) -> dict[str, Any]:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Extract name, email, and phone. Return one JSON object only."},
            {"role": "user", "content": message},
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(response.choices[0].message.content)


def moderate_customer_message(message: str) -> bool:
    response = client.moderations.create(model="omni-moderation-latest", input=message)
    return bool(response.results[0].flagged)


def embed_knowledge_text(text: str) -> list[float]:
    response = client.embeddings.create(model="text-embedding-3-large", input=text)
    return list(response.data[0].embedding)


def runtime_support_reply(question: str) -> str:
    selected_model = os.getenv("SUPPORT_MODEL", "gpt-4o")
    response = client.responses.create(model=selected_model, input=question)
    return response.output_text


TRIGGERS = {
    "summarize": lambda: summarize_support_ticket("The installer arrived two days late and the customer wants a revised timeline."),
    "classify": lambda: classify_sales_lead("A 200-person company has approved budget and needs installation within two weeks."),
    "extract": lambda: extract_contact_json("Maria Gomez can be reached at maria.gomez@example.com or 813-555-0192."),
    "moderate": lambda: moderate_customer_message("The customer is frustrated but made no threat of harm."),
    "embed": lambda: embed_knowledge_text("Warranty claims must be submitted within thirty days."),
    "runtime-support": lambda: runtime_support_reply("Can you confirm whether my installation is still scheduled for Friday?"),
}


def run_trigger(name: str):
    try:
        trigger = TRIGGERS[name]
    except KeyError as exc:
        raise ValueError(f"Unknown trigger: {name}") from exc
    return trigger()


def run_all_calls() -> dict[str, Any]:
    return {name: run_trigger(name) for name in TRIGGERS}
