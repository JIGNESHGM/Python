# program 11 :

# Write a program which accepts a sequence of comma
# separated 4 digit binary numbers as its input and then
# check whether they are divisible by 5 or not. The numbers
# that are divisible by 5 are to be printed in a comma
# separated sequence.

# Example:
# 0100,0011,1010,1001

# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# Define the function to check divisibility by 5

def is_divisible_by_5(binary_numbers):
    
    # Initialize an empty list to store the results
    results = []
    
    # Split the input string into a list of binary numbers
    binary_list = binary_numbers.split(",")
    
    # Iterate through each binary number in the list
    for binary in binary_list:
        
        # Convert the binary number to decimal
        decimal_number = int(binary,2)
        
        # Check if the decimal Number is divisible by 5 or not
        
        if decimal_number % 5 ==0:
            
            # If it is divisible by 5, append it to the results list
            results.append(binary)
        
    # Return The Result List
    return results

# Main Funcationdeclaration

def main():
    # Take input from the user
    binary_numbers = input("Enter a sequence of comma separated 4 digit binary numbers: ")
    
    # Call the function to check divisibility by 5
    divisible_numbers = is_divisible_by_5(binary_numbers)
    
    # Print the result as a comma separated string
    print(",".join(divisible_numbers))
    

# Call the main function
if __name__ == "__main__":
    main()