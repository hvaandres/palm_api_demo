from dotenv import load_dotenv
import os
import google.generativeai as palm
load_dotenv()

palm_api_key = os.getenv("Palm_API")

# Testing connection to PALM API
palm.configure(api_key=palm_api_key)

prompt = 'I need help to understand what is really going on with me'
scenarios = [
    ('Hello', 'Hi there!, how can I assists you today?'),
    ('I need help', 'Sure, I am here to help you. What is your problem? and how can I help you?'),
    ('I am feeling sad', 'I am sorry to hear that. Can you tell me more about it? I am here to listen to you'),
    ('I am feeling depressed', 'I am sorry to hear that. Can you tell me more about it? I am here to help to you'),
    ('I am feeling anxious', 'I am sorry to hear that. Can you tell me more about it? I am here to help to you understand what is going on with you'),
    ('I am feeling lonely', 'I am sorry to hear that. Can you tell me more about it? and what triggered this feeling?'),
    ('My feelings are hurt', 'I am sorry to hear that. Give me more details about it, and let me help you to understand what is going on with you'),
    ('I want to learn more about myself', 'Great, the first things to do is to understand your feelings and understand what is happening to you'),
]
# In order to talk to the model, we need to understand that 0 is the prompt and 1 is the response.
# In other words, 0 is yourself and 1 is the therapist.

response = palm.chat(messages=prompt, model='models/chat-bison-001', temperature=0.3, context='Speak Like a Therapist')
for message in response.messages:
    print(message['author'], message['content'])

