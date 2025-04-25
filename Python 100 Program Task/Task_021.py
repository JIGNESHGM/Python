# program 21 :

# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

# The numbers after the direction are steps. Please write a program
# to compute the distance from current position after a sequence
# of movement and original point. If the distance
# is a float, then just print the nearest integer.

# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


# Function to calculate the distance from the origin after a series of movements
def calculate_distance(movements):
    x, y = 0, 0  # Initialize the starting coordinates at the origin (0,0)
    
    for move in movements:  # Loop through each movement in the list
        direction, steps = move.split()  # Split the movement string into direction and step count
        steps = int(steps)  # Convert step count from string to integer
        
        # Adjust coordinates based on direction
        if direction.upper() == "UP":
            y += steps  # Move up increases Y coordinate
        elif direction.upper() == "DOWN":
            y -= steps  # Move down decreases Y coordinate
        elif direction.upper() == "LEFT":
            x -= steps  # Move left decreases X coordinate
        elif direction.upper() == "RIGHT":
            x += steps  # Move right increases X coordinate

    # Calculate Euclidean distance from origin to the final point
    return round((x**2 + y**2) ** 0.5)  # Return the rounded distance

# Main function to interact with the user
def main():
    print("Choose the robot movements by entering the corresponding number:")
    print("1. UP")
    print("2. DOWN")
    print("3. LEFT")
    print("4. RIGHT")
    print("Type 'STOP' to end input.")  # Instructions for the user

    movements = []  # List to store the sequence of movement commands

    while True:
        choice = input("Enter your choice (1/2/3/4 or STOP): ").strip().upper()  # Get user input for direction
        if choice == "STOP":
            break  # Exit loop if user types STOP

        if choice in ["1", "2", "3", "4"]:  # Check if the input is a valid direction option
            steps = input("Enter the number of steps: ").strip()  # Ask for number of steps
            if not steps.isdigit():  # Validate if input is a digit
                print("Invalid input for steps. Please enter a positive integer.")
                continue  # Skip and re-prompt if invalid

            steps = int(steps)  # Convert steps to integer

            # Convert numeric choice to movement direction and store it
            if choice == "1":
                movements.append(f"UP {steps}")
            elif choice == "2":
                movements.append(f"DOWN {steps}")
            elif choice == "3":
                movements.append(f"LEFT {steps}")
            elif choice == "4":
                movements.append(f"RIGHT {steps}")
        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or STOP.")  # Handle incorrect input

    # Call function to calculate distance and print result
    distance = calculate_distance(movements)
    print(f"The distance from the original point is: {distance}")

# Run the program
if __name__ == "__main__":
    main()
