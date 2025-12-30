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

def consistency_prompt(prompt: str, runs: int = 4)-> list :
    """
    Summary: This is useful for analyzing variability or consistency across multiple
        model runs.

    Args:
        prompt (str | list): The textual prompt to be passed to the experiment.
        image:The image input provided to the experiment (type depends on
        runs (int): Number of times to execute the experiment.

    Returns:
        list:
            A list containing the collected experiment results and the original prompt. 
    """
    output = []
    output.append(prompt)

    for _ in range(runs):
        result = run_experiment(
            prompt=output,
            image=image
        )
        if result:
            output.insert(0,result)

    return output