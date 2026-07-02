"""Cohere Python client."""
from __future__ import annotations

from typing import Any

__version__ = "5.11.0"


class ChatResponse:
    def __init__(self, model: str, text: str = "ok") -> None:
        self.text = text
        self.generation_id = "gen-local"
        self.finish_reason = "COMPLETE"
        self.meta = {"billed_units": {"input_tokens": 10, "output_tokens": 6}, "model": model}


class EmbedResponse:
    def __init__(self, model: str) -> None:
        self.embeddings = [[0.0] * 8]
        self.meta = {"model": model}


class RerankResult:
    def __init__(self, index: int, score: float) -> None:
        self.index = index
        self.relevance_score = score


class RerankResponse:
    def __init__(self) -> None:
        self.results = [RerankResult(0, 0.99), RerankResult(1, 0.5)]


class Client:
    def __init__(self, api_key: str | None = None, **_: Any) -> None:
        self.api_key = api_key

    def chat(self, *, model: str = "command-r", message: str | None = None, **_: Any) -> ChatResponse:
        return ChatResponse(model)

    def embed(self, *, model: str = "embed-english-v3.0", texts: Any = None, **_: Any) -> EmbedResponse:
        return EmbedResponse(model)

    def rerank(self, *, model: str = "rerank-english-v3.0", **_: Any) -> RerankResponse:
        return RerankResponse()


class ClientV2(Client):
    pass
