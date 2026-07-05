responses = {
"hello": "Hi! How can I help you?",
"hi": "Hello there!",
"how are you": "I am fine. Thanks!",
"what is your name": "I am a simple chatbot.",
"bye": "Goodbye!",
"thanks": "You are welcome!",
"what can you do": "I can answer simple questions.",
"who created you": "I was created using Python.",
"good morning": "Good morning!",
"good night": "Good night!"
}
while True:
    user_input = input("You: ").lower()
    if user_input == "exit":
        print("Chatbot: Goodbye!")
        break
    elif user_input in responses:
        print("Chatbot:", responses[user_input])
    else:
        print("Chatbot: I don't understand.")