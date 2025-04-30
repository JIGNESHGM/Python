# program 39 :

# Define a function which can generate a list
# where the values are square of
# numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

# Function to generate a list of squares of numbers within a user-defined range
def generate_square_list(start, end):
    # Initialize an empty list
    square_list = []
    
    # Loop through numbers in the user-defined range
    for num in range(start, end + 1):
        # Append the square of the number to the list
        square_list.append(num ** 2)
    
    # Return the list of squares
    return square_list

# Main function to get input and call the generate_square_list function
def main():
    # Get user input for the range
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    
    # Call the function and get the result
    square_list = generate_square_list(start, end)
    
    # Print the last 5 elements of the list
    print("The last 5 elements of the list are:", square_list[-5:])
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()
    

