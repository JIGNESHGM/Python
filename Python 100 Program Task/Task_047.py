# program 47 :

# Write a program which can map() and filter() to make
# a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.

# Funcation to generate a list of squares of even elements in the given list
def square_even_elements(input_list):
    # Filter even numbers and then square them
    return list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, input_list)))

# Main function to test the square_even_elements function
def main():
    input_list = list(map(int, input("Enter numbers separated by commas: ").split(',')))
    result = square_even_elements(input_list)
    print("The squares of the even elements in the list are:", result)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()