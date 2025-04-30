# program 37 :

# Define a function which can generate and print a list
# where the values are square of
# numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.

# Function to generate a list of squares of numbers between num1 and num2 (inclusive)
def generate_square_list(num1, num2):
    # Initialize an empty list to store the squares
    square_list = []
    
    # Check if the starting range is less than the ending range
    if num1 < num2:
        # Loop through the range from num1 to num2 (inclusive)
        for cnt in range(num1, num2 + 1):
            # Append the square of the current number to the list
            square_list.append(cnt ** 2)
        # Print the list of squares
        print(square_list)
    else:
        # Print an error message if the starting range is not less than the ending range
        print('Ending range must be greater than starting range')
        
# Main function to take user input and call the generate_square_list function
def main():
    try:
        # Take user input for the starting and ending range
        num1 = int(input('Enter starting range: '))
        num2 = int(input('Enter ending range: '))
        # Call the function to generate and print the list of squares
        generate_square_list(num1, num2)
    except ValueError:
        # Print an error message if the input is not a valid integer
        print('Check value')

# Call the main function to execute the program
if __name__ == '__main__':
    main()