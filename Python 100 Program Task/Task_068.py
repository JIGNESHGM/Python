# program 68:

# Please write a program using generator to
# print the even numbers between 0 and n in
# comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:

# 10

# Then, the output of the program should be:

# 0,2,4,6,8,10

# Hints:
# Use yield to produce the next value in generator.

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Function to generate even numbers up to n using a generator
def even_numbers_generator(n):
    for i in range(0, n + 1, 2):
        yield i
        
# Main function to test the even_numbers_generator function
def main():
    try:
        n = int(input("Enter a non-negative integer n: "))
        if n >= 0:
            even_numbers = even_numbers_generator(n)
            print(','.join(map(str, even_numbers)))
        else:
            print("Please enter a non-negative integer.")
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")
        
# Program starting point
if __name__ == '__main__':
    main()