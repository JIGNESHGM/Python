# program 80:

# Please write a program to randomly generate a
# list with5 numbers, which are divisible by 5 and 7 ,
# between 1 and 1000 inclusive.

# Hints:
# Use random.sample() to generate a list of random values.

# Funcation to generate a list of random numbers divisible by 5 and 7 between 1 and 1000 inclusive
import random

def generate_random_divisible_numbers(start, end, count):
    # Generate a list of numbers divisible by 5 and 7 between start and end inclusive
    divisible_numbers = [num for num in range(start, end + 1) if num % 5 == 0 and num % 7 == 0]
    
    # Randomly sample the specified count of numbers from the list
    random_divisible_numbers = random.sample(divisible_numbers, count)
    return random_divisible_numbers

# Main function to execute the program
def main():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))
    count = int(input("Enter the number of random numbers to generate: "))
    random_divisible_numbers = generate_random_divisible_numbers(start, end, count)
    print(f"List of {count} random numbers divisible by 5 and 7 between {start} and {end} inclusive: {random_divisible_numbers}")   
    
# Call the main function to run the program
if __name__ == "__main__":
    main()