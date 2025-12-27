import os

from dotenv import load_dotenv

# Loading env file for the gemini api key
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY", default="")

if not gemini_api_key:
    raise EnvironmentError("Google_gemini_key is not found.")