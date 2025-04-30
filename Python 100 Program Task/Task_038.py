# program 38 :

# Define a function which can generate a list
# where the values are square of
# numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

# Function to generate a list of squares of numbers from 1 to 20
def generate_square_list(start, end):
    # Initialize an empty list
    square_list = [i ** 2 for i in range(start, end + 1)]
    
    # Print the first 5 elements of the list
    print(square_list[:5])
    
# Main function to call the generate_square_list function
def main():
    # Define the range for generating squares
    start = int(input("Enter the start number (inclusive): "))
    end = int(input("Enter the end number (inclusive): "))
    # Call the function to generate and print the square list
    generate_square_list(start, end)

# Call the main function to execute the program
if __name__ == "__main__":
    main()
