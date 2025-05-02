# program 100:

# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?

# Hint:
# Use for loop to iterate all possible solutions.

# Function to solve the classic ancient Chinese puzzle
def solve_chickens_rabbits(heads, legs):
    # Iterate through all possible numbers of chickens (c) and rabbits (r)
    for c in range(heads + 1):
        r = heads - c  # Calculate the number of rabbits
        if 2 * c + 4 * r == legs:  # Check if the total number of legs matches
            return c, r  # Return the number of chickens and rabbits
    return None, None  # Return None if no solution is found

# Main function to execute the program
def main():
    heads = 35  # Total number of heads
    legs = 94   # Total number of legs
    chickens, rabbits = solve_chickens_rabbits(heads, legs)
    
    if chickens is not None and rabbits is not None:
        print(f"Number of chickens: {chickens}, Number of rabbits: {rabbits}")
    else:
        print("No solution found.")

# Call the main function to run the program
if __name__ == "__main__":
    main()