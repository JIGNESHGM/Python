# program 83:

# Please write a program to print the running
# time of execution of "1+1" for 100 times.

# Hints:
# Use timeit() function to measure the running time.

# Function to measure the running time of a given code snippet
import timeit

def measure_execution_time(code, number):
    # Measure the execution time of the code snippet
    execution_time = timeit.timeit(code, number=number)
    return execution_time

# Main function to execute the program
def main():
    # Take user input for the code snippet
    code_snippet = input("Enter the code snippet to measure execution time: ")
    
    # Take user input for the number of iterations
    try:
        number = int(input("Enter the number of iterations: "))
    except ValueError:
        print("Invalid input. Please enter an integer for the number of iterations.")
        return
    
    # Measure the execution time of the code snippet for the given number of iterations
    execution_time = measure_execution_time(code_snippet, number)
    
    # Print the execution time
    print(f"Execution time of '{code_snippet}' for {number} times: {execution_time} seconds")
    

# Call the main function to run the program
if __name__ == "__main__":
    main()