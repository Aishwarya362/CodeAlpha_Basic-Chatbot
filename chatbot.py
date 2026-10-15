def get_reply(user_input):
    """Match the user's message against known phrases and return a reply."""
    message = user_input.lower().strip()

    # Greetings
    if message in ("hello", "hi", "hey", "hiya"):
        return "Hi !"
    # Small talk
    elif message in ("how are you", "how are you?", "how's it going", "hows it going"):
        return "I'm fine, thanks !"
    elif message in ("what's your name", "whats your name", "who are you"):
        return "I'm PyBot, a simple rule-based chatbot."
    elif message == "help":
        return ("I understand: hello / how are you / what's your name / "
                "help / bye. Try one!")
    # Farewell
    elif message in ("bye", "goodbye", "see you", "quit", "exit"):
        return "Goodbye !"
    else:
        return "Sorry, I don't understand. Type 'help' to see what I can say."


def chat():
    print("PyBot: Hi ! I'm PyBot. Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ")
        reply = get_reply(user_input)
        print(f"PyBot: {reply}")
        if reply == "Goodbye !":
            break


if __name__ == "__main__":
    chat()
