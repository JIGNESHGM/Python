# program 29 :

# Define a function that can receive
# two integral numbers in string form
# and compute their sum and then print it in console.

# Hints:
# Use int() to convert a string to integer.



# Function to compute the sum of two numbers provided as strings
def compute_sum(num1_str, num2_str):
    """
    This function takes two numbers as strings, converts them to integers, and returns their sum.
    :param num1_str: First number as a string
    :param num2_str: Second number as a string
    :return: Sum of the two numbers as an integer
    """
    try:
        # Convert the input strings to integers after stripping any extra spaces
        num1 = int(num1_str.strip())
        num2 = int(num2_str.strip())
        return num1 + num2
    except ValueError:
        # Raise an error if the input strings cannot be converted to integers
        raise ValueError("Error: Please enter two valid integers.")

# Main function to handle user input and display the result
def main():
    """
    This function prompts the user for input, processes the input, and displays the result.
    """
    try:
        # Prompt the user to enter two numbers separated by a comma
        num1_str, num2_str = input("Enter two numbers separated by a comma: ").split(",")
        # Call the compute_sum function to calculate the sum
        result = compute_sum(num1_str, num2_str)
        # Display the result
        print(f"The sum of {num1_str.strip()} and {num2_str.strip()} is {result}")
    except ValueError as e:
        # Handle invalid input and display an error message
        print(e)

# Entry point of the program
if __name__ == "__main__":
    main()
