from agent.agent import Agent

def run_chat():
    # agent = Agent(model_name="google/flan-t5-small")
    agent = Agent(model_name="microsoft/phi-2")
    print(" Hugging Face Agent ready! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Agent: Goodbye ")
            break
        response = agent.respond(user_input)
        print("Agent:", response)

if __name__ == "__main__":
    run_chat()