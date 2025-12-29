from client import client

from prompt import image
from constant import MODEL_NAME, GENERATION_CONFIG

# This function returns the text from the client model
def run_experiment(prompts : str|None):
    '''
     Generate model output for the given prompts using the configured Gemini model.

    Args:
        prompts (str): Prompt or the contents send to the model.

    Returns:
        str: Generated text response from the model.
    '''

# Creating response with the help of client model,content and config
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[image, prompts],
        config=GENERATION_CONFIG
    )

    return response.text