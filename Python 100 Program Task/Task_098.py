# program 98:

# Please write a program which accepts a string from console and print the
# characters that have even indexes.

# Example:
# If the following string is given as input to the program:

# H1e2l3l4o5w6o7r8l9d

# Then, the output of the program should be:

# Helloworld

# Hints:
# Use list[::2] to iterate a list by step 2.

# Function to extract characters at even indexes from a string
def extract_even_indexed_characters(input_string):
    # Use slicing to get characters at even indexes
    return input_string[::2]

# Main function to execute the program
def main():
    # Prompt the user for input
    input_string = input("Please enter a string: ")
    
    # Extract characters at even indexes
    even_indexed_characters = extract_even_indexed_characters(input_string)
    
    # Print the result
    print(f"Characters at even indexes: {even_indexed_characters}")
    
# Call the main function to run the program
if __name__ == "__main__":
    main()