# program 99:

# Please write a program which prints all permutations of [1,2,3]

# Hints:
# Use itertools.permutations() to get permutations of list.

# Function to generate all permutations of a list
def generate_permutations(lst):
    from itertools import permutations
    return list(permutations(lst))

# Main function to execute the program
def main():
    # Define the list to be permuted
    input_list = list(map(int, input("Enter values separated by commas: ").split(',')))
    
    # Generate all permutations of the list
    permutations_list = generate_permutations(input_list)
    
    # Print all generated permutations
    for perm in permutations_list:
        print(perm)
        
# Call the main function to run the program
if __name__ == "__main__":
    main()