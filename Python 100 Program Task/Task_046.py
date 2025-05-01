# program 46 :

# Write a program which can map() to make a list whose elements
# are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.

# Funcation to generate a list of squares of elements in the given list
def square_elements(input_list):
    return list(map(lambda x: x ** 2, input_list))

# Main function to test the square_elements function
def main():
    input_list = list(map(int, input("Enter numbers separated by commas: ").split(',')))
    result = square_elements(input_list)
    print("The squares of the elements in the list are:", result)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()