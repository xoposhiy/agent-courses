"""Gemini client helper for HW3."""

import os
from google import genai

MODEL_NAME = "gemini-3.5-flash-lite"

# Use the following documentation to call the Gemini API:
#
#   sdk:     https://googleapis.github.io/python-genai/
#   api:     https://ai.google.dev/api/generate-content

def query_llm(prompt: str, temperature: float = 0.0) -> str:
    """Send a prompt to Gemini and return the raw string response."""
    api_key = os.getenv("GEMINI_API_KEY")
    raise NotImplementedError
