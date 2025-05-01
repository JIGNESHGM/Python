# program 65:

# Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=1

# with a given n input by console (n>0).

# Example:
# If the following n is given as input to the program:

# 5

# Then, the output of the program should be:

# 500

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Hints:
# We can define recursive function in Python.

# Function to compute f(n) using recursion
def compute_f(n):
    # Base case: if n is 0, return 1
    if n == 0:
        return 1
    # Recursive case: f(n) = f(n-1) + 100
    else:
        return compute_f(n - 1) + 100
    
# Main function to test the compute_f function
def main():
    # Input n from the user
    n = int(input("Enter a positive integer n: "))
    
    # Check if n is greater than 0
    if n > 0:
        result = compute_f(n)
        print("f({}) = {}".format(n, result))
    else:
        print("Please enter a positive integer greater than 0.")
        
# Call the main function to execute the program
if __name__ == "__main__":
    main()
