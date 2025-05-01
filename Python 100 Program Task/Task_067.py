# program 67:

# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program using list comprehension
# to print the Fibonacci Sequence
# in comma separated form with a given n input by console.

# Example:
# If the following n is given as input to the program:

# 7

# Then, the output of the program should be:

# 0,1,1,2,3,5,8,13

# Hints:
# We can define recursive function in Python.
# Use list comprehension to generate a list from an existing list.
# Use string.join() to join a list of strings.

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Function to compute the Fibonacci sequence up to n using iteration
def fibonacci_sequence(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

# Main function to test the fibonacci_sequence function
def main():
    try:
        n = int(input("Enter a non-negative integer n: "))
        if n >= 0:
            result = fibonacci_sequence(n)
            print(','.join(map(str, result)))
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")

# Program starting point 
if __name__ == '__main__':
    main()
