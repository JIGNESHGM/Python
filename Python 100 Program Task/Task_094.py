# program 94:

# With a given list [12,24,35,24,88,120,155,88,120,155], write a program
# to print this list after removing all duplicate values with original
# order reserved.

# Hints:
# Use set() to store a number of values without duplicate.

# Function to remove duplicates from a list while preserving order
def remove_duplicates(input_list):
    # Create an empty set to store unique elements
    seen = set()
    # Create a new list to store the result
    result = []
    
    # Iterate through the input list
    for item in input_list:
        # If the item is not in the seen set, add it to both seen and result
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Main function to execute the program
def main():
    # Input list
    # Prompt user to input comma-separated values
    user_input = input("Enter comma-separated values: ")
    
    # Split the input string into a list
    input_list = user_input.split(",")
    
    # Remove any non-numeric values and convert to integers
    input_list = [int(item) for item in input_list if item.strip().isdigit()]
    
    # Print the cleaned list
    print("Cleaned input list:", input_list)
    
    # Remove duplicates from the list
    result_list = remove_duplicates(input_list)
    
    # Print the result
    print("List after removing duplicates:", result_list)
    
# Call the main function to run the program
if __name__ == "__main__":
    main()