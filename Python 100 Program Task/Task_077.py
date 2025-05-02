# program 77:

# Please write a program to output a random number,
# which is divisible by 5 and 7, between 0 and 10
# inclusive using random module and list comprehension.

# Hints:
# Use random.choice() to a random element from a list.

# Function to generate a random number divisible by 5 and 7 between 0 and 10 inclusive
import random

def random_divisible_number(start, end):
    # Generate a list of numbers divisible by 5 and 7 between 0 and 10 inclusive
    divisible_numbers = [num for num in range(start, end) if num % 5 == 0 and num % 7 == 0]
    
    # Choose a random number from the list
    return random.choice(divisible_numbers)

# Main function to execute the program
def main():
    
    start = int(input("Enter the start of the range (inclusive): "))
    end = int(input("Enter the end of the range (exclusive): "))
    random_divisible = random_divisible_number(start, end)
    print(f"Random number between {start} and {end} inclusive divisible by 5 and 7: {random_divisible}")
    
# Call the main function to run the program
if __name__ == "__main__":
    main()