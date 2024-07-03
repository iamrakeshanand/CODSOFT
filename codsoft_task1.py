import random

# Define responses based on user inputs
responses = {
    "hello": "Hello! How can I help you?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but thanks for asking!",
    "bye": "Goodbye! Have a nice day.",
    "thanks": "You're welcome!",
    "what's your name?": "I'm just a simple chatbot.",
    "tell me a joke": "Why don't scientists trust atoms? Because they make up everything!",
    "how's the weather?": "I'm not sure, I'm just a bot!",
    "who created you?": "I was created by an awesome developer.",
    "default": "Sorry, I don't understand that."
}

# Function to handle user input and generate responses
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for case insensitivity
    
    # Simple pattern matching with if-else statements
    if user_input in responses:
        return responses[user_input]
    elif "thank" in user_input:
        return responses["thanks"]
    elif "bye" in user_input:
        return responses["bye"]
    else:
        return responses["default"]

# Main loop to interact with the chatbot
print("Welcome to the Simple Chatbot!")
print("Enter 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print(chatbot_response(user_input))
        break
    else:
        print("Bot:", chatbot_response(user_input))
