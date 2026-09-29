from tinyagent import LLM, TinyAgent

if __name__ == "__main__":
    llm = LLM()
    agent = TinyAgent(llm=llm)
    task = input("Ask a question to LLM: ")
    response = agent.run(task=task)
    print(response)
