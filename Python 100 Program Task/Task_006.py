# program006:

# Write a program that calculates and prints the value according to the
# given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a
# comma-separated sequence.

# Example
# Let us assume the following comma separated input sequence
# is given to the program:
# 100,150,180

# The output of the program should be:
# 18,22,24

# Hints:
# If the output received is in decimal form,
# it should be rounded off to its nearest value
# (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be
# assumed to be a console input.



import math

# Constants
C = 50
H = 30

# Function to calculate Q
def calculate_q(d_values):
    """
    Calculate the value of Q for a given list of D values using the formula:
        Q = √((2 * C * D) / H)
    where C and H are constants.

    Parameters:
    d_values (list of int): A list of integer values representing D.

    Returns:
    list of int: A list of integers representing the calculated Q values, rounded to the nearest whole number.

    Note:
    - The constants C and H must be defined in the global scope for this function to work.
    - The `math` module must be imported to use the `math.sqrt` function.
    """
    result = []
    for d in d_values:
        q = math.sqrt((2 * C * d) / H)
        result.append(round(q))
    return result

# Main program
if __name__ == "__main__":
    # Input from user
    input_values = input("Enter comma-separated values for D: ")
    try:
        d_values = list(map(int, input_values.split(',')))
    except ValueError:
        print("Invalid input. Please enter numbers separated by commas.")
        exit(1)
    
    # Calculate and print Q values
    q_values = calculate_q(d_values)
    print(",".join(map(str, q_values)))
