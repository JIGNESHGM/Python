# program 66:

# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program to compute the value
# of f(n) with a given n input by console.

# Example:
# If the following n is given as input to the program:

# 7

# Then, the output of the program should be:

# 13

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Hints:
# We can define recursive function in Python.

# Function to compute the Fibonacci number using iteration
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

# Main function to test the fibonacci function
def main():
    try:
        n = int(input("Enter a non-negative integer n: "))
        if n >= 0:
            result = fibonacci(n)
            print(f"f({n}) = {result}")
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

# Execute the main function
if __name__ == "__main__":
    main()
