# Necessary module
# pip install -q -U google-genai
# pip install python-dotenv

from dotenv import load_dotenv
import os

from google import genai
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.

# API key must be provided in .env file
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

print("Start chatting with the AI! Type 'goodbye' to stop.")


while True:
    user_input = input("You: ")
    
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=user_input
    )
    print("AI: ",response.text)
    if user_input.lower() == 'goodbye':
        break

print("Chat ended.")

