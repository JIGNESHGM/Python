# program 49 :

# Write a program which can map() to make a list whose
# elements are square of numbers between 1 and 20 (both included).

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.

# Function to generate a list of squares of numbers between 1 and 20 (both included)
def square_numbers_in_range(start, end):
    # Generate a list of squares of numbers in the given range
    return list(map(lambda x: x ** 2, range(start, end + 1)))

# Main function to test the square_numbers_in_range function
def main():
    start = int(input("Enter the start of the range (inclusive): "))
    end = int(input("Enter the end of the range (inclusive): "))

    result = square_numbers_in_range(start, end)
    print("The squares of numbers between", start, "and", end, "are:", result)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()