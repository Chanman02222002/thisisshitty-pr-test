"""Provider client construction for the platform service layer."""
from __future__ import annotations

import os

import boto3
import cohere
import google.generativeai as genai
import openai
from anthropic import Anthropic
from openai import AsyncOpenAI, AzureOpenAI, OpenAI

_OPENAI_KEY = os.getenv("OPENAI_API_KEY", "sk-local-dev")
openai.api_key = _OPENAI_KEY

client = OpenAI(api_key=_OPENAI_KEY)
async_client = AsyncOpenAI(api_key=_OPENAI_KEY)
azure_client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT", "https://example.openai.azure.com"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-06-01"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY", "local"),
)
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY", "local"))
co = cohere.Client(os.getenv("COHERE_API_KEY", "local"))
bedrock = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"))
genai.configure(api_key=os.getenv("GOOGLE_API_KEY", "local"))
