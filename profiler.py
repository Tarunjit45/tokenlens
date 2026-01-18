import json

class LLMCallProfiler:
    """
    Analyzes a single LLM call dictionary for token-related metrics.
    Uses word count as a proxy for token count.
    """
    def __init__(self, call_data):
        self.call_data = call_data
        self._prompt_data = call_data.get("prompt", {})

    def _count_tokens(self, text):
        """Counts words as a proxy for tokens."""
        if not text or not isinstance(text, str):
            return 0
        return len(text.split())

    @property
    def instruction_tokens(self):
        """Returns the token count of the system prompt."""
        return self._count_tokens(self._prompt_data.get("system_prompt"))

    @property
    def context_tokens(self):
        """Returns the token count of the context."""
        return self._count_tokens(self._prompt_data.get("context"))

    @property
    def user_query_tokens(self):
        """Returns the token count of the user query."""
        return self._count_tokens(self._prompt_data.get("user_query"))

    @property
    def prompt_tokens(self):
        """Returns the total token count of the prompt."""
        return self.instruction_tokens + self.context_tokens + self.user_query_tokens

    @property
    def completion_tokens(self):
        """Returns the token count of the completion."""
        return self._count_tokens(self.call_data.get("completion"))

    @property
    def system_prompt_content(self):
        """Returns the content of the system prompt."""
        return self._prompt_data.get("system_prompt", "")
