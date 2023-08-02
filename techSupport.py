from dotenv import load_dotenv
import os
import google.generativeai as palm
load_dotenv()

palm_api_key = os.getenv("Palm_API")

# Testing connection to PALM API
palm.configure(api_key=palm_api_key)

# Default values
defaults = {
    'model': 'models/chat-bison-001',
    'temperature': 0.25,
    'candidate_count': 1,
}

# Contexts
context = "Given a topic, write a response in a concise and professional manner."
examples = [
    ["Request access to my account",
     "Dear [Customer's name],\n\nThank you for contacting us. We have received your request and will get back to you as soon as possible.\n\nBest regards,\n\n[Your name]"
    ],
    [
     "I'm having trouble logging in",
     "I'm afraid to let you know that we don't know what could be the problem. However, you can provide us more detailed information, and we should be able to troubleshoot this issue for you."
    ],
    [
     "I do apologize for the inconvenience, but I don't remember my password",
     "You will need to go to the login page and click on the 'Forgot Password' link. You will be asked to enter your email address, and a new password will be sent to you."
    ],
    [
     "I reset my password, but I still can't log in",
     "Please provide me more details about the issue you are facing. I will be able to check the logs and see what could be the problem."   
    ]
]

messages = [
    "Request access to my account",
    "Sure, I will be happy to help you with that. Please provide me with your email address, and I will send you a link to reset your password.",
    "My email is the following [email address]",
    "Thanks for providing me with this information. I have sent you an email with a link to reset your password. Please check your inbox and follow the instructions.",
    "I tried to log in, but I still can't access my account",
    "Hmm, that's strange. I will check the logs and see what could be the problem. I will get back to you as soon as possible.",
    "Thank you for your help",
    "You are welcome. Please give me a few minutes to check the logs, and I will get back to you as soon as possible.",
    "It looks like your website has an issue with the login page",
    "Hmm, interesting. Please tell me more about the issue you are facing. And could you please send me a screenshot of the error message you are getting?",
]

print("Type 'quit' to exit the chat")
while True:
    user_input = input("You: ")
    if user_input == 'quit':
        break
    messages.append(user_input)
    response = palm.chat(messages=messages, **defaults, context=context, examples=examples)
    last_message = response.last
    # Chat with the model
    print("Chatbot:", last_message)
print("Conversation ended") # Returns the most recent request
