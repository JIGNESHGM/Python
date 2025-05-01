
# program 70:

# Please write assert statements to verify that
# every number in the list [2,4,6,8] is even.

# Hints:
# Use "assert expression" to make assertion.

# Funcation to check if all numbers in the list are even
def check_even_numbers(numbers):
    # Use assert to verify that each number is even
    for number in numbers:
        assert number % 2 == 0, f"{number} is not an even number."
        
# Main function to test the check_even_numbers function
def main():
    numbers = list(map(int, input("Enter numbers separated by commas: ").split(',')))
    try:
        check_even_numbers(numbers)
        print("All numbers in the list are even.")
    except AssertionError as e:
        print(e)
        
# Call the main function to execute the program
if __name__ == "__main__":
    main()