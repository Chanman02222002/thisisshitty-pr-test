"""edge_cases.py - hard AI call sites + decoys for the scanner.

Each EC* function is one detection challenge. Functions whose docstring starts
with "TRUE:" contain a real AI model call the scanner MUST find. Functions whose
docstring starts with "DECOY:" must NOT be flagged - they look like model calls
but are not. Ground truth for all of these lives in SCANNER_TRAINING_CONTEXT.md.

Everything here is runnable against the offline mock in fake_ai.py.
"""
from __future__ import annotations

import asyncio
import os
from typing import Any

from fake_ai import (
    ChatCompletion,
    OpenAI,
    OpenAI as LLM,          # EC05: aliased import
    async_client,
    client,
    db,                     # decoy
    http_session,           # decoy
)

# Module-level model config the calls reference indirectly.
DEFAULT_MODEL = "gpt-4"                                  # EC01 source
MODELS = {"fast": "gpt-4o-mini", "smart": "gpt-4o"}     # EC02 source


# EC01 -------------------------------------------------------------------------
def ec01_model_from_constant(note: str) -> str:
    """TRUE: model comes from a module-level constant, not a literal."""
    response = client.chat.completions.create(
        model=DEFAULT_MODEL,
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC02 -------------------------------------------------------------------------
def ec02_model_from_dict(note: str, tier: str = "smart") -> str:
    """TRUE: model resolved through a dict lookup."""
    response = client.chat.completions.create(
        model=MODELS[tier],
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC03 -------------------------------------------------------------------------
def ec03_model_from_fstring(note: str, variant: str = "mini") -> str:
    """TRUE: model name built with an f-string."""
    response = client.chat.completions.create(
        model=f"gpt-4o-{variant}",
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC04 -------------------------------------------------------------------------
def ec04_model_from_env(note: str) -> str:
    """TRUE: model chosen from the environment at runtime."""
    response = client.chat.completions.create(
        model=os.getenv("EC04_MODEL", "gpt-4-turbo"),
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC05 -------------------------------------------------------------------------
def ec05_aliased_client(note: str) -> str:
    """TRUE: client imported under an alias (OpenAI as LLM) and built locally."""
    local = LLM(api_key="unused")
    response = local.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC06 -------------------------------------------------------------------------
def ec06_client_built_inside_function(note: str) -> str:
    """TRUE: the client is constructed inside the function body."""
    inner = OpenAI()
    response = inner.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC07 -------------------------------------------------------------------------
def _llm_helper(prompt: str, model: str) -> str:
    """TRUE: the actual call lives in a generic helper; model is a parameter."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def ec07_call_via_helper(note: str) -> str:
    """Caller of _llm_helper - the call site is inside the helper above."""
    return _llm_helper(note, model="gpt-4o")


# EC08 -------------------------------------------------------------------------
async def ec08_async_completion(note: str) -> str:
    """TRUE: async client, awaited call."""
    response = await async_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC09 -------------------------------------------------------------------------
def ec09_streaming(note: str) -> str:
    """TRUE: streaming response (stream=True), assembled by iterating chunks."""
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": note}],
        stream=True,
    )
    return "".join(chunk.choices[0].delta.content for chunk in stream)


# EC10 -------------------------------------------------------------------------
def ec10_call_in_comprehension(notes: list[str]) -> list[str]:
    """TRUE: call buried inside a list comprehension."""
    return [
        client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": n}],
        ).choices[0].message.content
        for n in notes
    ]


# EC11 -------------------------------------------------------------------------
def ec11_call_in_lambda() -> str:
    """TRUE: call wrapped in a lambda."""
    ask = lambda q: client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": q}],
    ).choices[0].message.content
    return ask("ping")


# EC12 -------------------------------------------------------------------------
def ec12_kwargs_spread(note: str) -> str:
    """TRUE: arguments (including model) passed via **kwargs."""
    params: dict[str, Any] = {
        "model": "gpt-4o",
        "messages": [{"role": "user", "content": note}],
    }
    response = client.chat.completions.create(**params)
    return response.choices[0].message.content


# EC13 -------------------------------------------------------------------------
def _get_client() -> OpenAI:
    return OpenAI()


def ec13_factory_chain(note: str) -> str:
    """TRUE: call chained directly off a factory's return value."""
    response = _get_client().chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC14 -------------------------------------------------------------------------
def ec14_batch_api(note: str) -> Any:
    """TRUE: batch endpoint (no per-request model kwarg on the call itself)."""
    return client.batches.create(
        input_file_id="file_mock",
        endpoint="/v1/chat/completions",
        completion_window="24h",
    )


# EC15 -------------------------------------------------------------------------
def ec15_legacy_v0(note: str) -> str:
    """TRUE: legacy OpenAI v0 surface, openai.ChatCompletion.create."""
    response = ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC16 -------------------------------------------------------------------------
def _retry(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper


@_retry
def ec16_decorator_wrapped(note: str) -> str:
    """TRUE: the call lives inside a decorated function."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC17 -------------------------------------------------------------------------
def ec17_weird_formatting(note:str)->str:
    """TRUE: deliberately ugly formatting and tight spacing."""
    r=client.chat.completions.create(model="gpt-4o-mini",messages=[{"role":"user","content":note}]);return r.choices[0].message.content


# EC18 -------------------------------------------------------------------------
def ec18_two_calls_one_line(a: str, b: str) -> tuple[str, str]:
    """TRUE x2: two separate model calls on a single physical line."""
    x = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": a}]); y = client.chat.completions.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": b}])
    return x.choices[0].message.content, y.choices[0].message.content


# EC19 -------------------------------------------------------------------------
def ec19_ternary_model(note: str, urgent: bool = False) -> str:
    """TRUE: model selected by a ternary expression."""
    response = client.chat.completions.create(
        model="gpt-4o" if urgent else "gpt-4o-mini",
        messages=[{"role": "user", "content": note}],
    )
    return response.choices[0].message.content


# EC20 -------------------------------------------------------------------------
class SupportAgent:
    """TRUE: call uses self.client set up in __init__."""

    def __init__(self) -> None:
        self.client = OpenAI()
        self.model = "gpt-4o"

    def reply(self, note: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": note}],
        )
        return response.choices[0].message.content


# EC21 -------------------------------------------------------------------------
def ec21_commented_out(note: str) -> str:
    """DECOY: a commented-out call must not be flagged."""
    # response = client.chat.completions.create(
    #     model="gpt-4",
    #     messages=[{"role": "user", "content": note}],
    # )
    return "intentionally not calling the model"


# EC22 -------------------------------------------------------------------------
def ec22_model_name_in_text(note: str) -> str:
    """DECOY: 'gpt-4' appears only inside log/docstring text, not a call.

    We mention gpt-4 and claude-3-opus here on purpose; no API is invoked.
    """
    log_line = "would have used gpt-4o for: " + note
    return log_line


# EC23 -------------------------------------------------------------------------
def ec23_non_ai_create(warehouse: str) -> dict[str, Any]:
    """DECOY: .create() with a model= kwarg, but it's a database row, not AI."""
    record = db.records.create(model=warehouse, quantity=12)
    also = db.embeddings.create(vector_id="v-1")   # 'embeddings.create' bait
    return {"record": record, "also": also}


# EC24 -------------------------------------------------------------------------
def ec24_unrelated_model_key() -> dict[str, Any]:
    """DECOY: a dict with a 'model' key that is a truck, not an LLM."""
    config = {"model": "f-150", "year": 2024, "model_year": "gpt-4-lookalike"}
    return config


# EC25 -------------------------------------------------------------------------
def ec25_plain_webhook(payload: dict[str, Any]) -> dict[str, Any]:
    """DECOY: an HTTP POST to a non-AI endpoint."""
    return http_session.post("https://hooks.example.com/notify", json=payload)


# --------------------------------------------------------------------------- #
# Runnable registry - exercises every TRUE edge case (decoys excluded).
# --------------------------------------------------------------------------- #
def run_runnable_edge_cases() -> dict[str, Any]:
    agent = SupportAgent()
    results: dict[str, Any] = {
        "ec01": ec01_model_from_constant("late install"),
        "ec02": ec02_model_from_dict("budget approved"),
        "ec03": ec03_model_from_fstring("question"),
        "ec04": ec04_model_from_env("question"),
        "ec05": ec05_aliased_client("question"),
        "ec06": ec06_client_built_inside_function("question"),
        "ec07": ec07_call_via_helper("question"),
        "ec08": asyncio.run(ec08_async_completion("question")),
        "ec09": ec09_streaming("question"),
        "ec10": ec10_call_in_comprehension(["a", "b"]),
        "ec11": ec11_call_in_lambda(),
        "ec12": ec12_kwargs_spread("question"),
        "ec13": ec13_factory_chain("question"),
        "ec14": ec14_batch_api("question").id,
        "ec15": ec15_legacy_v0("question"),
        "ec16": ec16_decorator_wrapped("question"),
        "ec17": ec17_weird_formatting("question"),
        "ec18": ec18_two_calls_one_line("a", "b"),
        "ec19": ec19_ternary_model("question", urgent=True),
        "ec20": agent.reply("question"),
    }
    return results
