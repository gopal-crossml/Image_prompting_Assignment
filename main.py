from prompt import *
from run_experiment import run_experiment

# The main function runs the whole program
def main():
    output = run_experiment(prompt1)
    print("\n=== MODEL OUTPUT ===\n")
    print(output)
    
# Driver code
if __name__ == "__main__":
    main()