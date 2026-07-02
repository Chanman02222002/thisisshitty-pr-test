"""LangChain Anthropic chat model."""
from __future__ import annotations

from typing import Any

__version__ = "0.2.4"


class AIMessage:
    def __init__(self, content: str = "ok") -> None:
        self.content = content
        self.type = "ai"


class ChatAnthropic:
    def __init__(self, *, model: str | None = None, model_name: str | None = None,
                 max_tokens: int = 1024, temperature: float = 0.7, **_: Any) -> None:
        self.model = model or model_name or "claude-3-5-haiku-20241022"
        self.max_tokens = max_tokens
        self.temperature = temperature

    def invoke(self, _input: Any, **_: Any) -> AIMessage:
        return AIMessage()
