def get_response(user_input):
    user_input = user_input.lower()

    # Greeting
    if user_input in ["hello", "hi", "hey"]:
        return "Hello! How can I help you today?"

    # Basic questions
    elif user_input == "how are you":
        return "I'm feeling awesome today!"

    elif user_input == "what is your name":
        return "I'm your upgraded Python chatbot!"

    elif user_input == "what can you do":
        return "I can chat with you, tell jokes, and even do small tasks! Type 'help' to see tasks."

    # --- Small Talk ---
    elif user_input in ["what's up", "whats up"]:
        return "Just chatting with you!"

    elif user_input == "tell me a joke":
        return "Why don't programmers like nature? Too many bugs! 😂"

    elif user_input == "where are you from":
        return "I live inside your Python code!"

    elif user_input == "i'm bored" or user_input == "im bored":
        return "Try asking me to reverse a word or do a calculation!"

    # --- Tasks Section ---
    elif user_input == "help":
        return ("Here are things I can do:\n"
                "- add X and Y\n"
                "- multiply X and Y\n"
                "- reverse WORD\n"
                "- count WORD\n"
                "- small talk (hello, joke, etc.)")

    # Task: Add numbers
    elif user_input.startswith("add"):
        try:
            parts = user_input.replace("add", "").replace("and", "").split()
            num1 = int(parts[0])
            num2 = int(parts[1])
            return f"The sum is {num1 + num2}"
        except:
            return "Please use format: add 5 and 3"

    # Task: Multiply numbers
    elif user_input.startswith("multiply"):
        try:
            parts = user_input.replace("multiply", "").replace("and", "").split()
            num1 = int(parts[0])
            num2 = int(parts[1])
            return f"The result is {num1 * num2}"
        except:
            return "Use format: multiply 4 and 6"

    # Task: Reverse a word
    elif user_input.startswith("reverse"):
        word = user_input.replace("reverse", "").strip()
        if word:
            return f"Reversed: {word[::-1]}"
        else:
            return "Use format: reverse hello"

    # Task: Count characters
    elif user_input.startswith("count"):
        word = user_input.replace("count", "").strip()
        if word:
            return f"'{word}' has {len(word)} characters."
        else:
            return "Use format: count python"

    # Gratitude
    elif user_input in ["thanks", "thank you"]:
        return "You're welcome!"

    # Exit
    elif user_input == "bye":
        return "Goodbye! Come back soon!"

    # Default fallback
    else:
        return "I don't understand that. Type 'help' to see what I can do."


print("🤖 Chatbot with Small Talk + Tasks")
print("Type something to chat. Type 'bye' to exit.\n")

while True:
    user_text = input("You: ")
    response = get_response(user_text)
    print("Bot:", response)

    if user_text.lower() == "bye":
        break
