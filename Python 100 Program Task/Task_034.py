# program 34 :

# Define a function which can print a dictionary where the keys are numbers
# between 1 and 20 (both included) and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.

# Function to create a dictionary with numbers and their squares
def create_square_dict(start, end):
    square_dict = {}
    for num in range(start, end + 1):
        square_dict[num] = num ** 2
    return square_dict

# Main function to get user input and display the dictionary
def main():
    try:
        start = int(input("Enter the starting number (1-20): "))
        end = int(input("Enter the ending number (1-20): "))

        if 1 <= start <= 20 and 1 <= end <= 20 and start <= end:
            result = create_square_dict(start, end)
            print("The dictionary of squares from {} to {}: {}".format(start, end, result))
        else:
            print("Please enter numbers between 1 and 20, and ensure the starting number is less than or equal to the ending number.")
    except ValueError:
        print("Invalid input. Please enter integers only.")
        
# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()