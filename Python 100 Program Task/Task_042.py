# program 42 :

# With a given tuple (1,2,3,4,5,6,7,8,9,10),
# write a program to print the first half values
# in one line and the last half values in one line.

# Hints:
# Use [n1:n2] notation to get a slice from a tuple.

# Function to print the first and last half of a tuple
def print_tuple_half(tup):
    # Calculate the midpoint of the tuple
    mid = len(tup) // 2

    # Print the first half
    print("First half:", tup[:mid])

    # Print the last half
    print("Last half:", tup[mid:])
    
# Main function to demonstrate the functionality
def main():
    # Given tuple
    tup = tuple(map(int, input("Enter the tuple values separated by spaces: ").split()))

    # Call the function to print the halves
    print_tuple_half(tup)
    
# Entry point of the program
if __name__ == "__main__":
    main()