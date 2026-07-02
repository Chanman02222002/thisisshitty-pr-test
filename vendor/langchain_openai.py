"""LangChain OpenAI chat and embedding models."""
from __future__ import annotations

from typing import Any, Iterable

__version__ = "0.2.9"


class AIMessage:
    def __init__(self, content: str = "ok") -> None:
        self.content = content
        self.type = "ai"
        self.response_metadata: dict[str, Any] = {}


class ChatOpenAI:
    def __init__(self, *, model: str | None = None, model_name: str | None = None,
                 temperature: float = 0.7, **_: Any) -> None:
        self.model_name = model or model_name or "gpt-4o-mini"
        self.temperature = temperature

    def invoke(self, _input: Any, **_: Any) -> AIMessage:
        return AIMessage()

    def stream(self, _input: Any, **_: Any) -> Iterable[AIMessage]:
        yield AIMessage("o")
        yield AIMessage("k")

    def batch(self, inputs: list[Any], **_: Any) -> list[AIMessage]:
        return [AIMessage() for _ in inputs]


class OpenAIEmbeddings:
    def __init__(self, *, model: str = "text-embedding-3-small", **_: Any) -> None:
        self.model = model

    def embed_query(self, _text: str) -> list[float]:
        return [0.0] * 8

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [[0.0] * 8 for _ in texts]
