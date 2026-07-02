"""OpenAI Python client (v1 clients and legacy module-level resources)."""
from __future__ import annotations

from typing import Any, Iterable

__version__ = "1.51.0"

_DEFAULT_TEXT = "ok"
_JSON_CONTACT = '{"name": "Maria Gomez", "email": "maria.gomez@example.com", "phone": "813-555-0192"}'
_EMBED_DIM = 8


class OpenAIError(Exception):
    pass


class RateLimitError(OpenAIError):
    pass


class _Message:
    def __init__(self, content: str) -> None:
        self.content = content
        self.role = "assistant"
        self.tool_calls: list[Any] = []


class _Delta:
    def __init__(self, content: str) -> None:
        self.content = content
        self.role = "assistant"


class _Choice:
    def __init__(self, content: str) -> None:
        self.message = _Message(content)
        self.delta = _Delta(content)
        self.text = content
        self.index = 0
        self.finish_reason = "stop"


class _Usage:
    def __init__(self, prompt: int = 12, completion: int = 8) -> None:
        self.prompt_tokens = prompt
        self.completion_tokens = completion
        self.total_tokens = prompt + completion


class _EmbeddingRow:
    def __init__(self, vector: list[float]) -> None:
        self.embedding = vector
        self.index = 0
        self.object = "embedding"


class _ModerationCategory:
    def __init__(self, flagged: bool) -> None:
        self.flagged = flagged
        self.categories: dict[str, bool] = {}
        self.category_scores: dict[str, float] = {}


class ChatCompletionResponse:
    def __init__(self, model: str, text: str) -> None:
        self.id = "chatcmpl-local"
        self.object = "chat.completion"
        self.model = model
        self.choices = [_Choice(text)]
        self.usage = _Usage()

    def __iter__(self) -> Iterable["ChatCompletionResponse"]:
        for piece in (self.choices[0].message.content, ""):
            yield ChatCompletionResponse(self.model, piece)


class EmbeddingResponse:
    def __init__(self, model: str) -> None:
        self.object = "list"
        self.model = model
        self.data = [_EmbeddingRow([0.0] * _EMBED_DIM)]
        self.usage = _Usage(9, 0)


class ModerationResponse:
    def __init__(self, model: str, flagged: bool = False) -> None:
        self.id = "modr-local"
        self.model = model
        self.results = [_ModerationCategory(flagged)]


class ResponsesResponse:
    def __init__(self, model: str, text: str) -> None:
        self.id = "resp-local"
        self.model = model
        self.output_text = text
        self.output = [_Choice(text)]
        self.usage = _Usage()


class Batch:
    def __init__(self) -> None:
        self.id = "batch-local"
        self.status = "validating"
        self.endpoint = "/v1/chat/completions"


def _wants_json(response_format: Any) -> bool:
    if isinstance(response_format, dict):
        return response_format.get("type") == "json_object"
    return getattr(response_format, "type", None) == "json_object"


class _Completions:
    def create(self, *, model: str = "gpt-4o-mini", messages: Any = None,
               response_format: Any = None, stream: bool = False, **_: Any) -> ChatCompletionResponse:
        text = _JSON_CONTACT if _wants_json(response_format) else _DEFAULT_TEXT
        return ChatCompletionResponse(model, text)


class _Chat:
    def __init__(self) -> None:
        self.completions = _Completions()


class _Embeddings:
    def create(self, *, model: str = "text-embedding-3-small", input: Any = None, **_: Any) -> EmbeddingResponse:
        return EmbeddingResponse(model)


class _Moderations:
    def create(self, *, model: str = "omni-moderation-latest", input: Any = None, **_: Any) -> ModerationResponse:
        return ModerationResponse(model)


class _Responses:
    def create(self, *, model: str = "gpt-4o-mini", input: Any = None, **_: Any) -> ResponsesResponse:
        return ResponsesResponse(model, _DEFAULT_TEXT)


class _Batches:
    def create(self, **_: Any) -> Batch:
        return Batch()


class _Files:
    def create(self, **_: Any) -> Any:
        obj = Batch()
        obj.id = "file-local"
        return obj


class OpenAI:
    def __init__(self, *, api_key: str | None = None, base_url: str | None = None,
                 organization: str | None = None, timeout: float | None = None, **_: Any) -> None:
        self.api_key = api_key
        self.base_url = base_url
        self.chat = _Chat()
        self.embeddings = _Embeddings()
        self.moderations = _Moderations()
        self.responses = _Responses()
        self.batches = _Batches()
        self.files = _Files()

    def with_options(self, **_: Any) -> "OpenAI":
        return self


class AzureOpenAI(OpenAI):
    def __init__(self, *, azure_endpoint: str | None = None, api_version: str | None = None,
                 azure_deployment: str | None = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.azure_endpoint = azure_endpoint
        self.api_version = api_version


class _AsyncCompletions:
    async def create(self, *, model: str = "gpt-4o-mini", response_format: Any = None,
                     stream: bool = False, **_: Any) -> ChatCompletionResponse:
        text = _JSON_CONTACT if _wants_json(response_format) else _DEFAULT_TEXT
        return ChatCompletionResponse(model, text)


class _AsyncChat:
    def __init__(self) -> None:
        self.completions = _AsyncCompletions()


class _AsyncResponses:
    async def create(self, *, model: str = "gpt-4o-mini", **_: Any) -> ResponsesResponse:
        return ResponsesResponse(model, _DEFAULT_TEXT)


class _AsyncEmbeddings:
    async def create(self, *, model: str = "text-embedding-3-small", **_: Any) -> EmbeddingResponse:
        return EmbeddingResponse(model)


class AsyncOpenAI:
    def __init__(self, *, api_key: str | None = None, **_: Any) -> None:
        self.api_key = api_key
        self.chat = _AsyncChat()
        self.responses = _AsyncResponses()
        self.embeddings = _AsyncEmbeddings()


# --- legacy module-level resources (openai<1.0 style) ----------------------
api_key: str | None = None


class ChatCompletion:
    @staticmethod
    def create(*, model: str = "gpt-3.5-turbo", **_: Any) -> ChatCompletionResponse:
        return ChatCompletionResponse(model, _DEFAULT_TEXT)


class Completion:
    @staticmethod
    def create(*, model: str = "gpt-3.5-turbo-instruct", **_: Any) -> ChatCompletionResponse:
        return ChatCompletionResponse(model, _DEFAULT_TEXT)


class Embedding:
    @staticmethod
    def create(*, model: str = "text-embedding-ada-002", **_: Any) -> EmbeddingResponse:
        return EmbeddingResponse(model)


class Moderation:
    @staticmethod
    def create(*, model: str = "text-moderation-latest", **_: Any) -> ModerationResponse:
        return ModerationResponse(model)
