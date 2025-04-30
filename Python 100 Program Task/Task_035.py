# program 35 :

# Define a function which can generate a dictionary
# where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the
# values only.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to
# get key/value pairs.

# Funcation to generate a dictionary with keys as numbers and values as their squares
def generate_square_dict(start, end):
    square_dict = {}
    for num in range(start, end + 1):
        square_dict[num] = num ** 2
    return square_dict

# Main function to execute the program
def main():
    try:
        start = int(input("Enter starting range (1-20): "))
        end = int(input("Enter ending range (1-20): "))

        if 1 <= start <= 20 and 1 <= end <= 20 and start <= end:
            square_dict = generate_square_dict(start, end)
            print("The squares of numbers from {} to {} are:".format(start, end))
            for value in square_dict.values():
                print(value)
        else:
            print("Please enter valid numbers between 1 and 20.")
    except ValueError:
        print("Invalid input. Please enter integers only.")
        

# Entry point of the program
if __name__ == "__main__":
    main()