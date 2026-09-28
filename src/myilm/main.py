from llm import LLM
from response import parse_llm_response


if __name__ == "__main__":
    my_llm = LLM()
    llm_answer = my_llm.ask_llm("Hello, how are you?")
    response = parse_llm_response(llm_answer)
    print(response)
