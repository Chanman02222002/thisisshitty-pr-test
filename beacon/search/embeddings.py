"""Embedding generation for search."""
from __future__ import annotations

from beacon.llm.clients import client


def embed_document(text: str) -> list:
    """Embed document."""
    response = client.embeddings.create(model="text-embedding-3-large", input=text)
    return response.data[0].embedding


def vectorize_article(items: list[str]) -> list[list]:
    """Vectorize article."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-ada-002", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def encode_ticket(text: str) -> list:
    """Encode ticket."""
    response = client.embeddings.create(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def index_faq(items: list[str]) -> list[list]:
    """Index faq."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-3-large", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def embed_chunk(text: str) -> list:
    """Embed chunk."""
    response = client.embeddings.create(model="text-embedding-ada-002", input=text)
    return response.data[0].embedding


def vectorize_query(items: list[str]) -> list[list]:
    """Vectorize query."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-3-small", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def encode_passage(text: str) -> list:
    """Encode passage."""
    response = client.embeddings.create(model="text-embedding-3-large", input=text)
    return response.data[0].embedding


def index_document(items: list[str]) -> list[list]:
    """Index document."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-ada-002", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def embed_article(text: str) -> list:
    """Embed article."""
    response = client.embeddings.create(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def vectorize_ticket(items: list[str]) -> list[list]:
    """Vectorize ticket."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-3-large", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def encode_faq(text: str) -> list:
    """Encode faq."""
    response = client.embeddings.create(model="text-embedding-ada-002", input=text)
    return response.data[0].embedding


def index_chunk(items: list[str]) -> list[list]:
    """Index chunk."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-3-small", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def embed_query(text: str) -> list:
    """Embed query."""
    response = client.embeddings.create(model="text-embedding-3-large", input=text)
    return response.data[0].embedding


def vectorize_passage(items: list[str]) -> list[list]:
    """Vectorize passage."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-ada-002", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def encode_document(text: str) -> list:
    """Encode document."""
    response = client.embeddings.create(model="text-embedding-3-small", input=text)
    return response.data[0].embedding


def index_article(items: list[str]) -> list[list]:
    """Index article."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-3-large", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def embed_ticket(text: str) -> list:
    """Embed ticket."""
    response = client.embeddings.create(model="text-embedding-ada-002", input=text)
    return response.data[0].embedding


def vectorize_faq(items: list[str]) -> list[list]:
    """Vectorize faq."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-3-small", input=item)
        vectors.append(response.data[0].embedding)
    return vectors


def encode_chunk(text: str) -> list:
    """Encode chunk."""
    response = client.embeddings.create(model="text-embedding-3-large", input=text)
    return response.data[0].embedding


def index_query(items: list[str]) -> list[list]:
    """Index query."""
    vectors = []
    for item in items:
        response = client.embeddings.create(model="text-embedding-ada-002", input=item)
        vectors.append(response.data[0].embedding)
    return vectors
