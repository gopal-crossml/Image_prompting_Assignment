# Image prompting Assignment
A Lightweight python projectintegrating google gemini 3 flash for controlled text generation, exploring parameter tuning (temperature, top_p, max_tokens) across multiple prompting techniques and use this for getting vetter optimized output.

## :pushpin: Project Overview
The project consists of **Different prompt experiments**:
1. **Text Generation Experiments with different prompt techniques**
   - Few shot prompt technique
   - Role based prompt tecnique
   - Context based prompt technique
   - Role based prompt technique
   - Chain of thought prompt technique
   - Tree of thought prompt technique
---
## :hammer_and_wrench: Tech Stack
- **Language:** Python 3.10+
- **LLM:** Google Gemini
- **SDK:** `google-genai`, PILLOW
---
## :gear: Installation
1. Clone the repository
    ```bash
        https://github.com/gopal-crossml/Image_prompting_Assignment
        cd Image_prompting_Assignment
2. Create and activate a virtual environment (recommended)
    ```bash
        python -m venv venv
        source venv/bin/activate
3. Install dependencies
    ```bash
        pip install google-genai dotenv
4. :closed_lock_with_key: API Key Setup
    Replace API-KEY in the code with your Gemini API key:
    python
        client = get_client(api_key=gemini_api_key)
5. :arrow_forward: Usage
  :one: Text Generation Experiment
    This script explores how different prompts and parameters affect generated text.
        python main.py
    Prompts Used:
      -  All the prompts are available in the prompts.py file
      -  use all the prompts one by one and analyse the output
    Parameters Tuned:
      -  temperature
      -  top_p
      -  top_k
      -  max_output_tokens
:test_tube: Learning Outcomes
  -  Understand the impact of temperature on creativity
  -  Compare top_p vs top_k sampling
  -  Build intuition for prompt engineering
  -  Analysed different prompting techniques with output
