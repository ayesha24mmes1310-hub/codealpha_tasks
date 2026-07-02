# CodeAlpha Python Internship
# Task 4 - Basic Chatbot

while True:

    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine. Thanks!")

    elif user == "what is your name":
        print("Bot: I am CodeAlpha Chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")