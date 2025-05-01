# program 43 :

# Write a program to generate and print another
# tuple whose values are even numbers
# in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints:
# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.

# Function to generate a tuple of even numbers
def generate_even_tuple(start, end):
    # Check if the starting number is less than the ending number
    if start < end:
        # Create a range of numbers from start to end (inclusive)
        num_range = range(start, end + 1)
        # Initialize an empty list to store even numbers
        even_numbers = []
        # Iterate through the range of numbers
        for num in num_range:
            # Check if the number is even
            if num % 2 == 0:
                # Append the even number to the list
                even_numbers.append(num)
        # Convert the list of even numbers to a tuple and return it
        return tuple(even_numbers)
    else:
        print('Ending range must be greater than starting range')
        

# Main function to execute the program
def main():
    try:
        # Prompt the user for the starting and ending range
        start = int(input('Enter starting range: '))
        end = int(input('Enter ending range: '))
        # Call the function to generate the tuple of even numbers
        result = generate_even_tuple(start, end)
        # Print the resulting tuple of even numbers
        print(result)
    except ValueError:
        print('Check Value')
        
# Execute the main function if the script is run directly
if __name__ == '__main__':
    main()