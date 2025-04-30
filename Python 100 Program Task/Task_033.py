# program 33 :

# Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

# Funcation to create a dictionary with keys as numbers and values as their squares
def create_square_dict(start, end):
    square_dict = {}
    for num in range(start, end + 1):
        square_dict[num] = num ** 2
    return square_dict

# Main function to take user input and call the dictionary creation function
def main():
    try:
        start = int(input("Enter starting number (inclusive): "))
        end = int(input("Enter ending number (inclusive): "))
        if start > end:
            print("Starting number must be less than or equal to ending number.")
            return
        result_dict = create_square_dict(start, end)
        print("Generated dictionary:", result_dict)
    except ValueError:
        print("Invalid input. Please enter integers only.")
        
# Entry point of the script
if __name__ == "__main__":
    main()