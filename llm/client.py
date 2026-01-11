import os

class LLMClient:
    def __init__(self):
        self.provider = os.environ.get("LLM_PROVIDER", "openai")
        self.model = os.environ.get("LLM_MODEL", "gpt-4.1-mini")
        self.temperature = float(os.environ.get("LLM_TEMPERATURE", "0.0"))

    def complete_json(self, system_prompt: str, user_payload: dict) -> dict:
        raise NotImplementedError("Wire this to your LLM provider using JSON/function calling.")
