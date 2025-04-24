# program009 :
# Write a program that accepts sequence of lines as input and prints the
# lines after making all characters in the sentence capitalized.

# Suppose the following input is supplied to the

# program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


# Main Funcation Declaration

def main():
    # Prompt user for input
    print("Enter Lines of text (type 'exit' to finish):")
    
    # Initialize an empty list to store lines
    lines = []
    
    # Loop to read lines until 'exit' is entered
    while True:
        lines.append(input())
        if lines[-1].lower() == 'exit':
            break
        
    
    # Print each line in uppercase
    print("\nUppercase Lines:")
    
    for line in lines:
        if line.lower() == 'exit':
            break
        print(line.upper())
        

# Main function call
if __name__ == "__main__":
    main()