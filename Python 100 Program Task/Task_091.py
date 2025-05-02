# program 91:

# By using list comprehension, please write a program to print the list
# after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.
# Use enumerate() to get (index, value) tuple.

# Function to remove specific indices from a list
def remove_indices(input_list, indices_to_remove):
    # Use list comprehension to filter out elements at specified indices
    return [value for index, value in enumerate(input_list) if index not in indices_to_remove]

# Main function to execute the program
def main():
    # Input list
    input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    
    # Indices to remove (0th, 4th, and 5th)
    indices_to_remove = set(map(int, input("Enter indices to remove, separated by spaces: ").split()))
    
    # Remove specified indices from the list
    result_list = remove_indices(input_list, indices_to_remove)
    
    # Print the result
    print("List after removing specified indices:", result_list)
    
# Call the main function to run the program
if __name__ == "__main__":
    main()