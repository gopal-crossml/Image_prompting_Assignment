from google.genai import types

from prompt import *
# Defining the gemini model
MODEL_NAME = "gemini-3-flash-preview"

# config parameters
GENERATION_CONFIG = types.GenerateContentConfig(
    # system_instruction=prompt4,
    temperature=0.1,
    top_p=0.9,
    max_output_tokens=1000

)