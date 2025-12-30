from prompt import *
from run_experiment import run_experiment, consistency_prompt

# The main function runs the whole program
def main():
    output = run_experiment(prompt5)
    print("\n=== MODEL OUTPUT ===\n")
    print(output)
    
# Driver code
if __name__ == "__main__":
    main()

prompt_selection = prompt5


if prompt_selection == consistency_prompt:
    consistency_result = consistency_prompt(prompt5,image)
    for lst in consistency_result:
        print(f"-----output-----\n{lst}\n")
else:
    print(run_experiment,image)
