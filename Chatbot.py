import re

print("Chatbot: Hello! Welcome to Python Chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:

    user = input("You: ").lower()

    if re.search(r"hello|hi|hey", user):
        print("Chatbot: Hello! How can I help you?")

    elif re.search(r"how are you", user):
        print("Chatbot: I am fine. What about you?")

    elif re.search(r"your name|who are you", user):
        print("Chatbot: I am a simple Python chatbot.")

    elif re.search(r"college|study", user):
        print("Chatbot: Study hard and achieve your goals!")

    elif re.search(r"thank", user):
        print("Chatbot: You're welcome!")

    elif re.search(r"bye|exit", user):
        print("Chatbot: Goodbye! Have a nice day.")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")
