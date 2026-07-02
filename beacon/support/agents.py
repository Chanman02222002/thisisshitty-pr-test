"""Conversational assistant classes for the support workspace."""
from __future__ import annotations

from openai import OpenAI


class TicketAssistant:
    """TicketAssistant — conversational helper backed by an OpenAI model."""
    def __init__(self) -> None:
        self.client = OpenAI()
        self.model = "gpt-4"

    def reply(self, message: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": message}],
        )
        return response.choices[0].message.content


class EscalationCoach:
    """EscalationCoach — conversational helper backed by an OpenAI model."""
    def __init__(self) -> None:
        self.client = OpenAI()
        self.model = "gpt-4-turbo"

    def advise(self, context: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": context}],
        )
        return response.choices[0].message.content


class MacroSuggester:
    """MacroSuggester — conversational helper backed by an OpenAI model."""
    def __init__(self) -> None:
        self.client = OpenAI()
        self.model = "gpt-4o-mini"

    def suggest(self, text: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": text}],
        )
        return response.choices[0].message.content


class ToneRewriter:
    """ToneRewriter — conversational helper backed by an OpenAI model."""
    MODEL = "gpt-4o"

    def __init__(self) -> None:
        self.client = OpenAI()

    def rewrite(self, draft: str) -> str:
        response = self.client.chat.completions.create(
            model=self.MODEL,
            messages=[{"role": "user", "content": draft}],
        )
        return response.choices[0].message.content


class PolicyChecker:
    """PolicyChecker — conversational helper backed by an OpenAI model."""
    MODEL = "gpt-4"

    def __init__(self) -> None:
        self.client = OpenAI()

    def check(self, text: str) -> str:
        response = self.client.chat.completions.create(
            model=self.MODEL,
            messages=[{"role": "user", "content": text}],
        )
        return response.choices[0].message.content


class ResolutionPlanner:
    """ResolutionPlanner — conversational helper backed by an OpenAI model."""
    def __init__(self) -> None:
        self.client = OpenAI()
        self.model = "gpt-4o"

    def plan(self, summary: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": summary}],
        )
        return response.choices[0].message.content


class SentimentReader:
    """SentimentReader — conversational helper backed by an OpenAI model."""
    def __init__(self) -> None:
        self.client = OpenAI()
        self.model = "gpt-3.5-turbo"

    def read(self, text: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": text}],
        )
        return response.choices[0].message.content


class HandoffWriter:
    """HandoffWriter — conversational helper backed by an OpenAI model."""
    MODEL = "gpt-4-turbo"

    def __init__(self) -> None:
        self.client = OpenAI()

    def compose(self, notes: str) -> str:
        response = self.client.chat.completions.create(
            model=self.MODEL,
            messages=[{"role": "user", "content": notes}],
        )
        return response.choices[0].message.content


class FollowupDrafter:
    """FollowupDrafter — conversational helper backed by an OpenAI model."""
    def __init__(self) -> None:
        self.client = OpenAI()
        self.model = "gpt-4o"

    def draft(self, thread: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": thread}],
        )
        return response.choices[0].message.content


class KbSummarizer:
    """KbSummarizer — conversational helper backed by an OpenAI model."""
    def __init__(self) -> None:
        self.client = OpenAI()
        self.model = "gpt-4o-mini"

    def summarize(self, article: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": article}],
        )
        return response.choices[0].message.content
