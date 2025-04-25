# program 26 :

# Define a function which can compute the sum of two numbers.

# Hints:
# Define a function with two numbers as arguments.
# You can compute the sum in the function and return the value.


# Funcation to compute the sum of two numbers
def compute_sum(num1, num2):
    
    result = num1 + num2
    
    return result
    
    
# Defind Main Funcation

def main():
    
    # User input insert
    num1 = int(input("Enter Number 1 : "))
    num2 = int(input("Enter Number 2 : "))
    
    # Call the compute_sum function and store the result
    result = compute_sum(num1, num2)
    
    # Print the result
    print(f"The sum of {num1} and {num2} is: {result}")
    
# Call the main function
if __name__ == "__main__":
    main()
    

