# program 76:

# Please write a program to output a random even number
# between 0 and 10 inclusive using random module and list comprehension.

# Hints:
# Use random.choice() to a random element from a list.

# Function to generate a random even number between 0 and 10 inclusive
import random

def random_even_number(start, end):
    # Generate a list of even numbers between 0 and 10 inclusive
    even_numbers = [num for num in range(start, end) if num % 2 == 0]
    
    # Choose a random even number from the list
    return random.choice(even_numbers)

# Main function to execute the program
def main():
    
    start = int(input("Enter the start of the range (inclusive): "))
    end = int(input("Enter the end of the range (exclusive): "))
    random_even = random_even_number(start, end)
    print(f"Random even number between {start} and {end} inclusive: {random_even}")
    
# Call the main function to run the program
if __name__ == "__main__":
    main()