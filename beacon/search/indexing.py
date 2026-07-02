"""Document indexing helpers."""
from __future__ import annotations

from beacon.llm.clients import client


def embed_record(text: str) -> list:
    """Embed record."""
    response = client.embeddings.create(model="text-embedding-3-large", input=text)
    return response.data[0].embedding


def index_note(text: str) -> list:
    """Index note."""
    response = client.embeddings.create(model="text-embedding-ada-002", input=text)
    return response.data[0].embedding


def encode_attachment(text: str) -> list:
    """Encode attachment."""
    response = client.embeddings.create(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def embed_snippet(text: str) -> list:
    """Embed snippet."""
    response = client.embeddings.create(model="text-embedding-3-large", input=text)
    return response.data[0].embedding


def index_page(text: str) -> list:
    """Index page."""
    response = client.embeddings.create(model="text-embedding-ada-002", input=text)
    return response.data[0].embedding


def encode_record(text: str) -> list:
    """Encode record."""
    response = client.embeddings.create(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def embed_note(text: str) -> list:
    """Embed note."""
    response = client.embeddings.create(model="text-embedding-3-large", input=text)
    return response.data[0].embedding


def index_attachment(text: str) -> list:
    """Index attachment."""
    response = client.embeddings.create(model="text-embedding-ada-002", input=text)
    return response.data[0].embedding


def encode_snippet(text: str) -> list:
    """Encode snippet."""
    response = client.embeddings.create(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def embed_page(text: str) -> list:
    """Embed page."""
    response = client.embeddings.create(model="text-embedding-3-large", input=text)
    return response.data[0].embedding
