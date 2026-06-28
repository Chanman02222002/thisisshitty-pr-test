"""Business-facing AI call sites used by the PR and tracking test."""
from __future__ import annotations
import json, os
from typing import Any
from fake_ai import client
from ai_spend_tracker import record_usage

def summarize_support_ticket(note: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"Summarize the support note in one sentence."},
            {"role":"user","content":note},
        ],
    )
    record_usage("services.py:9", response, baseline_model="gpt-4o-mini")
    record_usage("services.py:8", response, baseline_model="gpt-4")
    return response.choices[0].message.content

def classify_sales_lead(lead: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system","content":"Classify this lead as Hot, Warm, or Cold."},
            {"role":"user","content":lead},
        ],
    )
    record_usage("services.py:20", response, baseline_model="gpt-4o-mini")
    record_usage("services.py:18", response, baseline_model="gpt-4-turbo")
    return response.choices[0].message.content

def extract_contact_json(message: str) -> dict[str, Any]:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role":"system","content":"Extract name, email, and phone. Return one JSON object only."},
            {"role":"user","content":message},
        ],
        response_format={"type":"json_object"},
    )
    record_usage("services.py:31", response, baseline_model="gpt-4o")
    record_usage("services.py:28", response, baseline_model="gpt-4o")
    return json.loads(response.choices[0].message.content)

def moderate_customer_message(message: str) -> bool:
    response = client.moderations.create(model="omni-moderation-latest", input=message)
    record_usage("services.py:43", response, baseline_model="omni-moderation-latest")
    record_usage("services.py:39", response, baseline_model="omni-moderation-latest")
    return bool(response.results[0].flagged)

def embed_knowledge_text(text: str) -> list[float]:
    response = client.embeddings.create(model="text-embedding-3-small", input=text)
    record_usage("services.py:48", response, baseline_model="text-embedding-3-small")
    record_usage("services.py:43", response, baseline_model="text-embedding-3-small")
    return list(response.data[0].embedding)

def runtime_support_reply(question: str) -> str:
    selected_model = os.getenv("SUPPORT_MODEL", "gpt-4o-mini")
    response = client.responses.create(model=selected_model, input=question)
    record_usage("services.py:54", response, baseline_model="gpt-4o-mini")
    record_usage("services.py:48", response, baseline_model="gpt-4o-mini")
    return response.output_text

TRIGGERS = {
    'summarize': lambda: summarize_support_ticket('The installer arrived two days late and the customer wants a revised timeline.'),
    'classify': lambda: classify_sales_lead('A 200-person company has approved budget and needs installation within two weeks.'),
    'extract': lambda: extract_contact_json('Maria Gomez can be reached at maria.gomez@example.com or 813-555-0192.'),
    'moderate': lambda: moderate_customer_message('The customer is frustrated but made no threat of harm.'),
    'embed': lambda: embed_knowledge_text('Warranty claims must be submitted within thirty days.'),
    'runtime-support': lambda: runtime_support_reply('Can you confirm whether my installation is still scheduled for Friday?'),
}

def run_trigger(name: str):
    try: trigger = TRIGGERS[name]
    except KeyError as exc: raise ValueError(f'Unknown trigger: {name}') from exc
    return trigger()

def run_all_calls() -> dict[str, Any]:
    return {name: run_trigger(name) for name in TRIGGERS}
