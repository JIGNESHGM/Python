# program 96:

# Please write a program which count and print the numbers of each
# character in a string input by console.

# Example:
# If the following string is given as input to the program:

# abcdefgabc

# Then, the output of the program should be:

# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

# Hints:
# Use dict to store key/value pairs.
# Use dict.get() method to lookup a key with default value.

# Function to count the occurrences of each character in a string
def count_characters(input_string):
    # Initialize an empty dictionary to store character counts
    char_count = {}
    
    # Iterate through each character in the input string
    for char in input_string:
        # Use dict.get() to get the current count, defaulting to 0 if not found
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count

# Main function to execute the program
def main():
    # Prompt the user for input
    input_string = input("Please enter a string: ")
    
    # Count the characters in the input string
    char_count = count_characters(input_string)
    
    # Print the character counts in the specified format
    for char, count in char_count.items():
        print(f"{char},{count}")
        

# Call the main function to run the program
if __name__ == "__main__":
    main()
