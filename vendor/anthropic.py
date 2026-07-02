"""Anthropic Python client (messages and legacy completions APIs)."""
from __future__ import annotations

from typing import Any

__version__ = "0.39.0"

HUMAN_PROMPT = "\n\nHuman:"
AI_PROMPT = "\n\nAssistant:"


class _TextBlock:
    def __init__(self, text: str) -> None:
        self.text = text
        self.type = "text"


class _Usage:
    def __init__(self) -> None:
        self.input_tokens = 14
        self.output_tokens = 9


class Message:
    def __init__(self, model: str, text: str = "ok") -> None:
        self.id = "msg-local"
        self.model = model
        self.role = "assistant"
        self.content = [_TextBlock(text)]
        self.stop_reason = "end_turn"
        self.usage = _Usage()


class Completion:
    def __init__(self, model: str) -> None:
        self.model = model
        self.completion = "ok"
        self.stop_reason = "stop_sequence"


class _Messages:
    def create(self, *, model: str = "claude-3-5-haiku-20241022", max_tokens: int = 512,
               messages: Any = None, system: Any = None, stream: bool = False, **_: Any) -> Message:
        return Message(model)


class _Completions:
    def create(self, *, model: str = "claude-2.1", **_: Any) -> Completion:
        return Completion(model)


class Anthropic:
    def __init__(self, *, api_key: str | None = None, **_: Any) -> None:
        self.api_key = api_key
        self.messages = _Messages()
        self.completions = _Completions()


class _AsyncMessages:
    async def create(self, *, model: str = "claude-3-5-haiku-20241022", **_: Any) -> Message:
        return Message(model)


class AsyncAnthropic:
    def __init__(self, *, api_key: str | None = None, **_: Any) -> None:
        self.api_key = api_key
        self.messages = _AsyncMessages()
