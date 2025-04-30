# program 28 :

# Define a function that can convert a integer
# into a string and print it in console.

# Hints:
# Use str() to convert a number to string.

# Define a function to convert a list of integers into a list of strings
def int_list_to_str_list(int_list):
    # Convert each integer in the list to a string
    str_list = [str(num) for num in int_list]
    return str_list

# Main function declaration
def main():
    # Get comma-separated integer values from the user
    int_values = input("Enter comma-separated integer values: ")
    
    # Convert the input string into a list of integers
    int_list = [int(num.strip()) for num in int_values.split(",")]
    
    # Function call to convert integers to strings
    str_list = int_list_to_str_list(int_list)
    
    # Print the list of strings
    print("Your integer values as strings are: ", str_list)

# Main function call
if __name__ == "__main__":
    main()
