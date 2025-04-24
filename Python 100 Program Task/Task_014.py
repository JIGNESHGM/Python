# program 14 :

# Write a program that accepts a sentence and
# calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


# Funcation to count upper and lower case latters

def count_case(sentance):
    
    # Veriabel Declaration in counters
    upper_count = 0
    lower_count = 0
    
    # Count of upper and lower case latters
    
    for chr in sentance:
        
        # Checking if the letter is upper case
        if chr.isupper():
            upper_count +=1
        elif chr.islower():
            lower_count +=1
    
    # Returning the count of upper and lower case letters
    
    return upper_count, lower_count


# Main Funcation Createion

def main():
    
    # Taking input for the user
    sentance = str(input("Enter a sentance : "))
    
    # calling the count_case function and storing the result in veriabel
    upper_count, lower_count = count_case(sentance)
    
    # Printing the result 
    print("UPPER CASE : ", upper_count)
    print("LOWER CASE : ", lower_count)
    
# Main function Execution
if __name__ == "__main__":
    
    # Main function call
    main()