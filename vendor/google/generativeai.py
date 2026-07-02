"""Google Generative AI (Gemini) client."""
from __future__ import annotations

from typing import Any

__version__ = "0.8.3"

_api_key: str | None = None


def configure(*, api_key: str | None = None, **_: Any) -> None:
    global _api_key
    _api_key = api_key


class GenerationConfig:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(kwargs)


class _Response:
    def __init__(self, text: str = "ok") -> None:
        self.text = text
        self.candidates = [type("C", (), {"content": text})()]
        self.usage_metadata = type("U", (), {
            "prompt_token_count": 12, "candidates_token_count": 7, "total_token_count": 19})()


class GenerativeModel:
    def __init__(self, model_name: str, *_: Any, generation_config: Any = None, **__: Any) -> None:
        self.model_name = model_name
        self.generation_config = generation_config

    def generate_content(self, *_: Any, **__: Any) -> _Response:
        return _Response()

    async def generate_content_async(self, *_: Any, **__: Any) -> _Response:
        return _Response()

    def start_chat(self, **_: Any) -> "_Chat":
        return _Chat(self)


class _Chat:
    def __init__(self, model: GenerativeModel) -> None:
        self._model = model

    def send_message(self, *_: Any, **__: Any) -> _Response:
        return _Response()


class _EmbedResult(dict):
    def __init__(self) -> None:
        super().__init__(embedding=[0.0] * 8)


def embed_content(*, model: str = "text-embedding-004", content: Any = None, **_: Any) -> dict[str, Any]:
    return _EmbedResult()
