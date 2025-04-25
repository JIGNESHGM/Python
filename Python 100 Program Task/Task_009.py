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


# Funcation declaration in convert string in Capital

def convert_to_uppercase(sentence):
    
    # convert each Sentance to uppercase 
    uppur_case = sentence.upper()
    # Return result 
    
    return uppur_case

# Main Funcation Declaration


def main():
    setance = str(input("Enter a setance : "))
    
    # Funcation call In uppercase
    result = convert_to_uppercase(setance)
    
    # Print the result
    print(result)
    

if __name__ == "__main__":
    # Main function call
    main()
    