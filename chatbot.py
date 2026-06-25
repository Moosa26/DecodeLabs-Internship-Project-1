responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hey! What can I do for you?",
    "how are you": "I'm just a program, but I'm running smoothly! How about you?",
    "what is your name": "I'm RuleBot, a simple rule-based chatbot built for DecodeLabs Project 1.",
    "what can you do": "I can chat with you using predefined rules. Try saying hello, asking my name, or saying bye!",
    "help": "You can talk to me using simple phrases like 'hello', 'how are you', or 'bye' to exit.",
    "thank you": "You're welcome! Happy to help.",
    "thanks": "Anytime! Let me know if you need anything else.",
}

EXIT_COMMANDS = {"bye", "exit", "quit"}


def get_response(user_input: str) -> str:
    return responses.get(user_input, "I do not understand. Could you rephrase that?")


def run_chatbot():
    print("=" * 50)
    print(" RuleBot - Rule-Based AI Chatbot (Project 1)")
    print(" Type 'bye', 'exit', or 'quit' to end the chat.")
    print("=" * 50)

    while True:
        raw_input_text = input("You: ")

        clean_input = raw_input_text.lower().strip()

        if clean_input in EXIT_COMMANDS:
            print("Bot: Goodbye! Have a great day.")
            break

        reply = get_response(clean_input)
        print(f"Bot: {reply}")


if __name__ == "__main__":
    run_chatbot()
