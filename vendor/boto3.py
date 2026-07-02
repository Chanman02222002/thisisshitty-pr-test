"""AWS SDK for Python (Bedrock Runtime and general service clients)."""
from __future__ import annotations

import io
import json
from typing import Any

__version__ = "1.35.0"


class _StreamingBody(io.BytesIO):
    pass


class _BedrockRuntime:
    def invoke_model(self, *, modelId: str, body: Any = None, **_: Any) -> dict[str, Any]:
        payload = {
            "content": [{"type": "text", "text": "ok"}],
            "usage": {"input_tokens": 12, "output_tokens": 7},
            "results": [{"outputText": "ok", "tokenCount": 7}],
            "generations": [{"text": "ok"}],
            "generation": "ok",
            "outputText": "ok",
        }
        return {"body": _StreamingBody(json.dumps(payload).encode("utf-8")),
                "contentType": "application/json"}

    def invoke_model_with_response_stream(self, *, modelId: str, body: Any = None, **_: Any) -> dict[str, Any]:
        chunk = {"chunk": {"bytes": json.dumps({"outputText": "ok"}).encode("utf-8")}}
        return {"body": [chunk], "contentType": "application/json"}


class _GenericClient:
    """Generic AWS service client (s3, dynamodb, sqs, ...)."""

    def __getattr__(self, _name: str):
        def _op(**kwargs: Any) -> dict[str, Any]:
            return {"ResponseMetadata": {"HTTPStatusCode": 200}, **kwargs}
        return _op


def client(service_name: str, *_: Any, **__: Any) -> Any:
    if service_name in ("bedrock-runtime", "bedrock"):
        return _BedrockRuntime()
    return _GenericClient()


def resource(service_name: str, *_: Any, **__: Any) -> Any:
    return _GenericClient()
