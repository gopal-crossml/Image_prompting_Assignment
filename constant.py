from google.genai import types

from prompt import *
# Defining the gemini model
MODEL_NAME = "gemini-3-flash-preview"

# config parameters
GENERATION_CONFIG = types.GenerateContentConfig(
    system_instruction = system_instruction,
    temperature=0.1,
    top_p=0.9,
    max_output_tokens=2000

)