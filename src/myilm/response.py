from dataclasses import dataclass
import json
from urllib.request import Request

import urllib


@dataclass
class LLMResponse:
	content: str = ""
	reasoning: str = None
	tool_call: dict = None
	metadata: dict = None

def parse_llm_response(model_response: Request) -> LLMResponse:
    """
    Parse the model response and generate an LLMResponse object.

    Args:
        model_response (dict): The response dictionary obtained from the model request.

    Returns:
        Response: An instance of the Response class containing the content, reasoning, tool_call, and metadata.
    """

    with model_response as response:
        data = json.loads(response.read())
    
    content = data.get("message", {}).get("content", "")
    reasoning = data.get("message", {}).get("reasoning", None)
    tool_call = data.get("message", {}).get("tool_calls", None) 
    metadata = data.get("message", {}).get("metadata", None)

    return LLMResponse(content=content, reasoning=reasoning, tool_call=tool_call, metadata=metadata)