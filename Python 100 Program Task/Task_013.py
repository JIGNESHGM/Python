# program 13 :

# Write a program that accepts a sentence and
# calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


# Funcation created to count letters and digits

def count_letters_and_digits(string):
    
    # initialize a dictionary to store the count of letters and digits
    
    latters, digits = 0, 0
    
    # iterate through each character in the string
    
    for char in string:
        
        # Condition Chake if the character is a letter or digit
        if char.isalpha():
                latters += 1
        elif char.isdigit():
            digits += 1
        
    # return the counts as a tuple
    return latters, digits

# Main Funcation Declaration 

def main():
    
    # Take User input 
    try:
        string = str(input ("Enter a string : "))
        latters, digits = count_letters_and_digits(string)
        print("LETTERS : ", latters)
        print("DIGITS : " , digits)
    # Handle ValueError exception
    except ValueError:
        print ('Check Input')
        return
    
# Call the main function
if __name__ == '__main__':
    main()