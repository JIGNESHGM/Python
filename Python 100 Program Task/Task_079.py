import random

# program 79:

# Please write a program to randomly generate a list
# with 5 even numbers between 100 and 200 inclusive.

# Hints:
# Use random.sample() to generate a list of random values.

# Function to generate a list of 5 random even numbers between 100 and 200 inclusive
def generate_random_even_numbers(start, end, count):
    # Generate a list of even numbers between start and end inclusive
    even_numbers = [num for num in range(start, end + 1) if num % 2 == 0]
    
    # Randomly sample the specified count of even numbers from the list
    random_even_numbers = random.sample(even_numbers, count)
    return random_even_numbers

# Main function to execute the program
def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    count = int(input("Enter the number of random even numbers to generate: "))
    random_even_numbers = generate_random_even_numbers(start, end, count)
    print(f"List of {count} random even numbers between {start} and {end} inclusive: {random_even_numbers}")
    
# Call the main function to run the program
if __name__ == "__main__":
    main()