# pip install -q -U google-genai
# pip install python-dotenv
from dotenv import load_dotenv
import os

from google import genai
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)