# program 69:

# Please write a program using generator to print
# the numbers which can be divisible by 5 and 7
# between 0 and n in comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:

# 100

# Then, the output of the program should be:

# 0,35,70

# Hints:
# Use yield to produce the next value in generator.

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Function to generate numbers divisible by 5 and 7 up to n using a generator
def divisible_by_5_and_7_generator(n):
    for i in range(0, n + 1):
        if i % 5 == 0 and i % 7 == 0:
            yield i
            
# Main function to test the divisible_by_5_and_7_generator function
def main():
    try:
        n = int(input("Enter a non-negative integer n: "))
        if n >= 0:
            divisible_numbers = divisible_by_5_and_7_generator(n)
            print(','.join(map(str, divisible_numbers)))
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")
        
# Program starting point
if __name__ == '__main__':
    main()