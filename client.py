from google import genai

from cred import gemini_api_key

# Function for creating client
client = genai.Client(api_key=gemini_api_key)

