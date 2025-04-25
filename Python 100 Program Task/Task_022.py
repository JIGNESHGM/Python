# program 22 :

# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and
# Python 3? Read Python 2 or Python 3.

# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# Funcation to compute frequency of words
def compute_frequency(input_string):
    # Split the input string into words
    words = input_string.split()
    
    # Create a dictionary to store the frequency of each word
    frequency = {}
    
    # Count the frequency of each word
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    # Sort the dictionary by keys (words) and return the result
    sorted_frequency = dict(sorted(frequency.items()))
    return sorted_frequency

# Main function to take input and display the frequency
def main():
    # Input string
    input_string = input("Enter a string: ")
    
    # Compute the frequency of words
    frequency = compute_frequency(input_string)
    
    # Display the frequency of each word
    for word, count in frequency.items():
        print(f"{word}:{count}")
        
# Call the main function
if __name__ == "__main__":
    main()