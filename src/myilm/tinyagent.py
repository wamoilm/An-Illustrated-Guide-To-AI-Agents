from myilm.llm import LLM
from myilm.response import Trajectory, parse_llm_response


class TinyAgent:
    def __init__(self, llm: LLM):
        self.llm = llm
        self.memory = None
        self.tools = None
        self.planner = None
        self.trajectory = Trajectory()

    def run(self, task: str):
        """
        Run the TinyAgent on a given task.

        Args:
            task (str): The task to be performed by the agent.
        """
        self.trajectory.initialize(task)
        # Here you would implement the logic for the agent to perform the task
        # using its LLM, memory, tools, and planner.
        return self._step(task)

    def _step(self, task: str) -> str:
        """
        Perform a single step in the agent's reasoning process.

        Args:
            task (str): The current task or query being processed.
        """
        # Here you would implement the logic for a single reasoning step
        # using the LLM and other components of the agent.
        message = task
        response = self.llm.ask_llm(message)
        parsed_response = parse_llm_response(response)
        return parsed_response.content

    def _execute_action(self, action: dict) -> str:
        """
        Execute a given action using the agent's tools.

        Args:
            action (dict): The action to be executed, typically containing tool information.
        """
        # Here you would implement the logic to execute the action using the agent's tools.
        # This is a placeholder for demonstration purposes.
        return "Action executed"  # Placeholder return value
