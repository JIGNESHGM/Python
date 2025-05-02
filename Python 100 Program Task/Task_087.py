# program 87:

# Please write a program to print the list after
# removing delete even numbers in [5,6,77,45,22,12,24].

# Hints:
# Use list comprehension to delete a bunch of element from a list.

# Function to remove even numbers from a list
def remove_even_numbers(input_list):
    # Use list comprehension to filter out even numbers
    return [num for num in input_list if num % 2 != 0]

# Main function to execute the program
def main():
    # Input list
    # Take user input as a comma-separated string
    user_input = input("Enter list items (comma-separated): ")
    
    # Convert the input string to a list, filtering out non-numeric values
    input_list = [
        float(item) if '.' in item else int(item)
        for item in user_input.split(',')
        if item.strip().replace('.', '', 1).isdigit()
    ]
    
    # Remove even numbers from the list
    result_list = remove_even_numbers(input_list)
    
    # Print the result
    print("List after removing even numbers:", result_list)
    
# Call the main function to run the program
if __name__ == "__main__":
    main()