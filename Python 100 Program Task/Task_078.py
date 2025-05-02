# program 78:

# Please write a program to generate a list
# with 5 random numbers between 100 and 200 inclusive.

# Hints:
# Use random.sample() to generate a list of random values.

# Function to generate a list of 5 random numbers between 100 and 200 inclusive
import random
def generate_random_numbers(start, end, count):
    # Generate a list of random numbers between 100 and 200 inclusive
    random_numbers = random.sample(range(start, end + 1), count)
    return random_numbers

# Main function to execute the program
def main():
    start = int(input("Enter the start of the range (inclusive): "))
    end = int(input("Enter the end of the range (inclusive): "))
    count = int(input("Enter the number of random numbers to generate: "))
    random_numbers = generate_random_numbers(start, end, count)
    print(f"List of {count} random numbers between {start} and {end} inclusive: {random_numbers}")
    
# Call the main function to run the program
if __name__ == "__main__":
    main()