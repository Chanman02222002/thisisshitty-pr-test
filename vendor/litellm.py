"""litellm — unified completion/embedding interface."""
from __future__ import annotations

from typing import Any

__version__ = "1.52.0"

drop_params = True
set_verbose = False


class _Message:
    def __init__(self, content: str) -> None:
        self.content = content
        self.role = "assistant"


class _Choice:
    def __init__(self, content: str) -> None:
        self.message = _Message(content)
        self.finish_reason = "stop"


class _EmbeddingRow(dict):
    def __init__(self, vector: list[float]) -> None:
        super().__init__(embedding=vector, index=0)
        self.embedding = vector


class ModelResponse:
    def __init__(self, model: str, text: str = "ok") -> None:
        self.id = "cmpl-local"
        self.model = model
        self.choices = [_Choice(text)]
        self.usage = {"prompt_tokens": 11, "completion_tokens": 7, "total_tokens": 18}


class EmbeddingResponse:
    def __init__(self, model: str) -> None:
        self.model = model
        self.data = [_EmbeddingRow([0.0] * 8)]


def completion(*, model: str = "gpt-4o-mini", messages: Any = None, **_: Any) -> ModelResponse:
    return ModelResponse(model)


async def acompletion(*, model: str = "gpt-4o-mini", messages: Any = None, **_: Any) -> ModelResponse:
    return ModelResponse(model)


def embedding(*, model: str = "text-embedding-3-small", input: Any = None, **_: Any) -> EmbeddingResponse:
    return EmbeddingResponse(model)


def batch_completion(*, model: str = "gpt-4o-mini", messages: Any = None, **_: Any) -> list[ModelResponse]:
    rows = messages or [None]
    return [ModelResponse(model) for _ in rows]
