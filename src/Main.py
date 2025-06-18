from TTA import AgentState, app

def print_stream(stream):
    last_message = None
    for s in stream:
        message = s["messages"][-1]
        content = getattr(message, "content", None)
        if content is not None:
            last_message = content
        else:
            last_message = str(message)
    if last_message is not None:
        print(f"Agent: {last_message}")

def get_user_input() -> str:
    return input("You: ")

def main():
    print("Welcome to Task Tracker Assistant! Type 'exit' to quit.")
    thread_id = "main-thread-1"
    while True:
        user_message = get_user_input()
        if user_message.strip().lower() == "exit":
            print("Goodbye!")
            break
        init_state = AgentState(messages=[user_message])
        print_stream(
            app.stream(
                init_state,
                {"configurable": {"thread_id": thread_id}},
                stream_mode="values"
            )
        )

if __name__ == "__main__":
    main()