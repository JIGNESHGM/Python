# program 97:

# Please write a program which accepts a string from console and print it
# in reverse order.

# Example:
# If the following string is given as input to the program:

# rise to vote sir

# Then, the output of the program should be:

# ris etov ot esir

# Hints:
# Use list[::-1] to iterate a list in a reverse order.

# Function to reverse a string
def reverse_string(input_string):
    # Reverse the string using slicing
    return input_string[::-1]

# Main function to execute the program
def main():
    # Prompt the user for input
    input_string = input("Please enter a string: ")
    
    # Reverse the string
    reversed_string = reverse_string(input_string)
    
    # Print the reversed string
    print(f"Reversed string: {reversed_string}")
    
# Call the main function to run the program
if __name__ == "__main__":
    main()