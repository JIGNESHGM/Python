# program 40 :

# Define a function which can generate a list
# where the values are square of
# numbers between 1 and 20 (both included).
# Then the function needs to print all values
# except the first 5 elements in the list.

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use [n1:n2] to slice a list

# Function to generate a list of squares of numbers
def generate_square_list(start, end):
    square_list = []
    for num in range(start, end + 1):
        square_list.append(num ** 2)
    return square_list

# Function to print the list excluding the first 5 elements
def print_excluding_first_five(square_list):
    print("List excluding the first 5 elements:")
    print(square_list[5:])
    
# Main function to execute the program
def main():
    start = int(input("Enter starting range (inclusive): "))
    end = int(input("Enter ending range (inclusive): "))
    square_list = generate_square_list(start, end)
    print_excluding_first_five(square_list)
    
# Entry point of the program
if __name__ == "__main__":
    main()