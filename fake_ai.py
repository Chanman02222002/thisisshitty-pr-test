"""fake_ai.py - offline mock AI SDKs for the scanner fixture.

This fakes just enough of the OpenAI, Anthropic, Google Gemini, litellm and
LangChain surfaces so every call site in this repo runs with no network access
and no API keys. The scanner under test reads these call sites *statically*;
the mocks exist only so CI (pytest / compileall) stays green and so the
fixture is runnable end to end.

Nothing here talks to a real provider. `model=` arguments are echoed back on
the response so tests and the training ground-truth can assert on them.
"""
from __future__ import annotations

from typing import Any

_MOCK_TEXT = "mock-response"
_EMBED_DIM = 8
_JSON_CONTACT = '{"name": "Maria Gomez", "email": "maria.gomez@example.com", "phone": "813-555-0192"}'


# --------------------------------------------------------------------------- #
# A single flexible response object that satisfies every SDK's accessors.
# --------------------------------------------------------------------------- #
class _Usage:
    def __init__(self, prompt_tokens: int = 11, completion_tokens: int = 7) -> None:
        # OpenAI names
        self.prompt_tokens = prompt_tokens
        self.completion_tokens = completion_tokens
        self.total_tokens = prompt_tokens + completion_tokens
        # Anthropic names
        self.input_tokens = prompt_tokens
        self.output_tokens = completion_tokens
        # Google names
        self.prompt_token_count = prompt_tokens
        self.candidates_token_count = completion_tokens
        self.total_token_count = prompt_tokens + completion_tokens


class _Message:
    def __init__(self, content: str) -> None:
        self.content = content
        self.role = "assistant"


class _Choice:
    def __init__(self, content: str) -> None:
        self.message = _Message(content)
        self.delta = _Message(content)   # streaming chunk shape
        self.text = content              # legacy completion shape
        self.finish_reason = "stop"


class _ContentBlock:
    def __init__(self, text: str) -> None:
        self.text = text
        self.type = "text"


class _EmbeddingItem:
    def __init__(self, vector: list[float]) -> None:
        self.embedding = vector
        self.index = 0


class _ModerationResult:
    def __init__(self, flagged: bool = False) -> None:
        self.flagged = flagged
        self.categories: dict[str, bool] = {}


class MockResponse:
    """One object shaped like every provider's response at once."""

    def __init__(self, model: str = "mock-model", text: str = _MOCK_TEXT) -> None:
        self.model = model
        self.id = "resp_mock"
        self.usage = _Usage()
        self.choices = [_Choice(text)]                 # OpenAI chat / completions
        self.content = [_ContentBlock(text)]           # Anthropic messages
        self.output_text = text                        # OpenAI Responses API
        self.text = text                               # Gemini generate_content
        self.data = [_EmbeddingItem([0.0] * _EMBED_DIM)]   # OpenAI embeddings
        self.results = [_ModerationResult(False)]      # OpenAI moderations
        self.output = [_Choice(text)]

    def __iter__(self):
        # Streaming: yield a couple of chunks shaped like the response.
        for piece in (self.output_text, ""):
            yield MockResponse(self.model, piece)


def _json_object_requested(response_format: Any) -> bool:
    if isinstance(response_format, dict):
        return response_format.get("type") == "json_object"
    return getattr(response_format, "type", None) == "json_object"


# --------------------------------------------------------------------------- #
# OpenAI v1 synchronous client:  client.chat.completions.create(...) etc.
# --------------------------------------------------------------------------- #
class _Completions:
    def create(self, *, model: str = "gpt-4o-mini", messages: Any = None,
               response_format: Any = None, stream: bool = False, **_: Any) -> MockResponse:
        text = _JSON_CONTACT if _json_object_requested(response_format) else _MOCK_TEXT
        return MockResponse(model, text)


class _Chat:
    def __init__(self) -> None:
        self.completions = _Completions()


class _Moderations:
    def create(self, *, model: str = "omni-moderation-latest", input: Any = None, **_: Any) -> MockResponse:
        return MockResponse(model)


class _Embeddings:
    def create(self, *, model: str = "text-embedding-3-small", input: Any = None, **_: Any) -> MockResponse:
        return MockResponse(model)


class _Responses:
    def create(self, *, model: str = "gpt-4o-mini", input: Any = None, **_: Any) -> MockResponse:
        return MockResponse(model)


class _Batches:
    def create(self, **_: Any) -> MockResponse:
        return MockResponse("batch")


class OpenAI:
    """Mirrors `from openai import OpenAI`."""

    def __init__(self, *_: Any, **__: Any) -> None:
        self.chat = _Chat()
        self.moderations = _Moderations()
        self.embeddings = _Embeddings()
        self.responses = _Responses()
        self.batches = _Batches()


# --------------------------------------------------------------------------- #
# OpenAI async client:  await async_client.chat.completions.create(...)
# --------------------------------------------------------------------------- #
class _AsyncCompletions:
    async def create(self, *, model: str = "gpt-4o-mini", **_: Any) -> MockResponse:
        return MockResponse(model)


class _AsyncChat:
    def __init__(self) -> None:
        self.completions = _AsyncCompletions()


class _AsyncResponses:
    async def create(self, *, model: str = "gpt-4o-mini", **_: Any) -> MockResponse:
        return MockResponse(model)


class AsyncOpenAI:
    def __init__(self, *_: Any, **__: Any) -> None:
        self.chat = _AsyncChat()
        self.responses = _AsyncResponses()


# --------------------------------------------------------------------------- #
# Legacy OpenAI v0:  openai.ChatCompletion.create(model=...)
# --------------------------------------------------------------------------- #
class ChatCompletion:
    @staticmethod
    def create(*, model: str = "gpt-3.5-turbo", **_: Any) -> MockResponse:
        return MockResponse(model)


# --------------------------------------------------------------------------- #
# Anthropic:  Anthropic().messages.create(model="claude-...")
# --------------------------------------------------------------------------- #
class _AnthropicMessages:
    def create(self, *, model: str = "claude-3-opus", **_: Any) -> MockResponse:
        return MockResponse(model)


class Anthropic:
    def __init__(self, *_: Any, **__: Any) -> None:
        self.messages = _AnthropicMessages()


# --------------------------------------------------------------------------- #
# Google Gemini:  genai.GenerativeModel("gemini-...").generate_content(...)
# --------------------------------------------------------------------------- #
class GenerativeModel:
    def __init__(self, model_name: str, *_: Any, **__: Any) -> None:
        self._model_name = model_name

    def generate_content(self, *_: Any, **__: Any) -> MockResponse:
        return MockResponse(self._model_name)


class _Genai:
    GenerativeModel = GenerativeModel

    def configure(self, **_: Any) -> None:
        pass


genai = _Genai()


# --------------------------------------------------------------------------- #
# litellm:  litellm.completion(model=...) / litellm.embedding(model=...)
# --------------------------------------------------------------------------- #
class _Litellm:
    def completion(self, *, model: str = "gpt-4o", **_: Any) -> MockResponse:
        return MockResponse(model)

    def embedding(self, *, model: str = "text-embedding-3-small", **_: Any) -> MockResponse:
        return MockResponse(model)


litellm = _Litellm()


# --------------------------------------------------------------------------- #
# LangChain:  ChatOpenAI(model="gpt-4o").invoke(...)
# --------------------------------------------------------------------------- #
class ChatOpenAI:
    def __init__(self, *, model: str | None = None, model_name: str | None = None, **_: Any) -> None:
        self.model = model or model_name or "gpt-4o-mini"

    def invoke(self, *_: Any, **__: Any) -> MockResponse:
        return MockResponse(self.model)


# --------------------------------------------------------------------------- #
# Non-AI decoys: objects that *look* like AI clients but are not.
# --------------------------------------------------------------------------- #
class _FakeTable:
    """A database-ish table whose .create() has nothing to do with AI."""

    def create(self, **_: Any) -> dict[str, Any]:
        return {"id": 1, "status": "created"}


class _FakeDB:
    def __init__(self) -> None:
        self.records = _FakeTable()
        self.embeddings = _FakeTable()   # named to bait the scanner


class _FakeHTTPSession:
    """A requests-like session; .post() is a plain webhook, not a model call."""

    def post(self, url: str, **_: Any) -> dict[str, Any]:
        return {"url": url, "status_code": 200}


db = _FakeDB()
http_session = _FakeHTTPSession()


# Default ready-to-use clients (module-level, the common real-world pattern).
client = OpenAI()
async_client = AsyncOpenAI()
