# program 75:

# Please generate a random float where the
# value is between 5 and 95 using Python math module.

# Hints:
# Use random.random() to generate a random float in [0,1].

# Function to generate a random float between 5 and 95
def generate_random_float(start, end):
    import random
    # Generate a random float between 5 and 95
    random_float = random.uniform(start, end)
    return random_float

# Main function to test the generate_random_float function
def main():
    start = int(input("Enter the start of the range (inclusive): "))
    end = int(input("Enter the end of the range (inclusive): "))
    random_float = generate_random_float(start, end)
    print("Random float between {} and {}: {}".format(start, end, random_float))
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()