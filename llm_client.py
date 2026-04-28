"""LLM client helpers.

Provides a simple `call_llm` function that posts to a local LLM HTTP endpoint.
A thin `LLMClient` wrapper is kept for backward compatibility.
"""

import requests


def call_llm(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=120,
        )
        response.raise_for_status()
        return response.json().get('response')
    except Exception as e:
        return f"LLM Error: {str(e)}"


class LLMClient:
    """Thin wrapper around `call_llm` for compatibility with existing code."""

    def __init__(self):
        pass

    def prompt(self, prompt_text: str) -> str:
        return call_llm(prompt_text)
