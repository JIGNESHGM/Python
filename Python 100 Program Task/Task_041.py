# program 41 :

# Define a function which can generate and print
# a tuple where the value are square of
# numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.

# Function to generate a tuple of squares of numbers from 1 to 20
def generate_square_tuple(start, end):
    # Create an empty list to store squares
    squares_list = []
    
    # Loop through numbers from start to end
    for num in range(start, end + 1):
        # Append the square of the number to the list
        squares_list.append(num ** 2)
    
    # Convert the list to a tuple and return it
    return tuple(squares_list)

# Main function to execute the program
def main():
    # Define the range of numbers
    start = int(input("Enter the start number (inclusive): "))
    end = int(input("Enter the end number (inclusive): "))
    
    # Generate the tuple of squares
    square_tuple = generate_square_tuple(start, end)
    
    # Print result 
    print("Tuple of squares from {} to {}: {}".format(start, end, square_tuple))
    
# Call the main function to run the program
if __name__ == "__main__":
    main()