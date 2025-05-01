# program 48 :

# Write a program which can filter() to make a list
# whose elements are even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

# Function to generate a list of even numbers between 1 and 20 (both included)
def even_numbers_in_range(start, end):
    # Filter even numbers in the given range
    return list(filter(lambda x: x % 2 == 0, range(start, end + 1)))

# Main function to test the even_numbers_in_range function
def main():
    start = int(input("Enter the start of the range (inclusive): "))
    end = int(input("Enter the end of the range (inclusive): "))

    result = even_numbers_in_range(start, end)
    print("The even numbers between", start, "and", end, "are:", result)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()