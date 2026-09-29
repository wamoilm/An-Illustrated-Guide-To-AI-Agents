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

@dataclass
class Step:
     thought: str = ""
     action: dict = None
     observation: str = ""
     answer: str = ""
     metadata: dict = None


class Trajectory:
    def __init__(self):
        self.runs = []

    def initialize(self, query: str) -> None:
        """
        Initialize a new trajectory run with the given query.
        """
        self.runs.append({
            "query": query,
            "steps": []})

    def add_step(self, response: LLMResponse, observation: str = None) -> None:
        """Record a model step and its observed outcome in the current trajectory.

        Args:
            response (LLMResponse): The language model response containing the
                reasoning, tool call, answer, and metadata for this step.
            observation (str, optional): An optional observation to attach to the
                step when the model interacts with the environment or tool output.

        Returns:
            None: The step is appended to the current trajectory run.
        """
        # Add thought
        step = Step(
            thought=response.reasoning,
            action=response.tool_call,
            observation=observation,
            answer=response.content,
            metadata=response.metadata
        )
        # Add Action/Observation/Answer
        if observation is not None:
            step.observation = observation
            step.action = response.tool_call
        else:
             step.answer = response.content
        self.runs[-1]["steps"].append(step)

    def get_steps(self):
        return self.steps