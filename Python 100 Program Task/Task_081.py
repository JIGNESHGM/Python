# program 81:

# Please write a program to randomly print
# an integer number between 7 and 15 inclusive.

# Hints:
# Use random.randrange() to a random integer in a given range.

# Function to generate a random integer between 7 and 15 inclusive
def generate_random_integer(start, end):
    import random
    return random.randint(start, end)

# Main function to execute the program
def main():
    start = int(input("Enter the start of the range (inclusive): "))
    end = int(input("Enter the end of the range (inclusive): "))
    random_integer = generate_random_integer(start, end)
    print(f"Random integer between {start} and {end} inclusive: {random_integer}")
    
# Call the main function to run the program
if __name__ == "__main__":
    main()
