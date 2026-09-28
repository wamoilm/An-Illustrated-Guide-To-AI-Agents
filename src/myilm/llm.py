import json
from urllib.request import Request, urlopen


class LLM:
    """A simple wrapper around an LLM API."""

    def __init__(self, model: str = "gemma4:e2b", user_input: str = ""):
        self.model = model
        self.user_input = "how are you?"

    def ask_llm(self, messages: list[dict]) -> json:
        """Generate a response from the LLM given a list of messages."""
        url = "http://localhost:11434/api/chat"
        headers = {"Content-Type": "application/json"}
        request_data = json.dumps({
            "model": self.model,
            "messages": [{"role": "user", "content": self.user_input}],
            "stream": False,
        }).encode("utf-8")

        request = Request(url, data=request_data, headers=headers, method="POST")
        response = urlopen(request)
        return response
