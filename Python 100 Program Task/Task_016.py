# program 16 :

# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# Funcation Create Odd Number List

def create_odd_number_list(values):
    
    # Veriabel Delclaration in List
    result = []
    
    # Loop for each number in the list
    for num in values:
        
        # Check if the number is odd
        if int(num) % 2 != 0:
            
            # Append the odd number to the result list
            result.append(num)
            
    # Return the list of odd numbers
    return ",".join(result)

# Main Function
def main():
    
    # Try block to handle exceptions
    try:
        
        # Input from user
        values = list(map(int, input("Enter numbers separated by commas: ").split(",")))
        
        # Call the function to create odd number list
        odd_numbers = create_odd_number_list(values)
        
        # Print the result
        print(odd_numbers)
        
    # Exception handling for ValueError
    except ValueError:
        print('Check Value')
        
# Call the main function
if __name__ == '__main__':
    main()