# program 45 :

# Write a program which can filter even numbers in
# a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.

# Function to filter even numbers from a list
def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))

# Main function to execute the program
def main():
    # List of numbers from 1 to 10
    numbers = list(map(int, input("Enter a list of numbers separated by commas: ").split(',')))
    
    # Filter even numbers using the filter_even_numbers function
    even_numbers = filter_even_numbers(numbers)
    
    # Print the filtered even numbers
    print("Even numbers in the list:", even_numbers)
    
# Entry point of the program
if __name__ == "__main__":
    main()