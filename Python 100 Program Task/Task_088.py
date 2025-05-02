# program 88:

# By using list comprehension, please write a program
# to print the list after removing delete numbers
# which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.

# Function to remove numbers divisible by 5 and 7 from a list
def remove_divisible_numbers(input_list):
    # Use list comprehension to filter out numbers divisible by 5 and 7
    return [num for num in input_list if num % 5 != 0 and num % 7 != 0]

# Main function to execute the program
def main():
    # Input list
    input_list = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    
    # Remove numbers divisible by 5 and 7 from the list
    result_list = remove_divisible_numbers(input_list)
    
    # Print the result
    print("List after removing numbers divisible by 5 and 7:", result_list)
    
# Call the main function to run the program