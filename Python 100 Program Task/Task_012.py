# program 12 :

# Write a program, which will find all such numbers
# between 1000 and 3000 (both included) such
# that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on
# a single line.

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.



# User-defined function to check if a number is even

def is_even(num):
    
    # Converting the number to string to iterate through earch digit
    num_str = str(num)
    
    # Checking if each digit is even
    for digit in num_str:
        if int(digit) % 2 != 0:
            return False
    return True

# Main Funcation Declaration

def main(start, end):
    # List to store the even number 
    even_numbers = []
    
    # Looping through the range of numbers
    
    for num in range (start,end + 1):
        
        # Checking if the number is even
        if is_even(num):
            even_numbers.append(str(num))
    
    # Returning the list of even numbers
    return ",".join(even_numbers)

# Main function Execution
if __name__ == "__main__":
    
    # Taking input from user
    start = int(input("Enter the starting number : "))
    end = int(input("Enter the ending number : "))
    
    # Main Funcation call Withe perameters and result store in result veriabel 
    result = main(start, end)
    
    # Print the result 
    print("The even Numbers are : ", result)