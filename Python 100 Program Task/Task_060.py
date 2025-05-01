# program 60 :

# Write a program which accepts a sequence
# of words separated by whitespace as input to print
# the words composed of digits only.

# Example:
# If the following words is given as input to the program:

# 2 cats and 3 dogs.

# Then, the output of the program should be:

# ['2', '3']

# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# Hints:
# Use re.findall() to find all substring using regex.

# Function to find all words composed of digits only
def find_digit_words(input_string):
    import re
    # Use regex to find all words composed of digits only
    return re.findall(r'\b\d+\b', input_string)

# Main function to test the find_digit_words function
def main():
    # Input string from the user
    input_string = input("Enter a sequence of words separated by whitespace: ")
    
    digit_words = find_digit_words(input_string)
    print(digit_words)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()