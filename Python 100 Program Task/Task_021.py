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


# Funcation to calculate distance
def calculate_distance(movements):
    x, y = 0, 0
    for move in movements:
        direction, steps = move.split()
        steps = int(steps)
        if direction == "UP":
            y += steps
        elif direction == "DOWN":
            y -= steps
        elif direction == "LEFT":
            x -= steps
        elif direction == "RIGHT":
            x += steps
    return round((x**2 + y**2) ** 0.5)

# Main function
def main():
    movements = []
    while True:
        try:
            movement = input()
            if not movement:
                break
            movements.append(movement)
        except EOFError:
            break

    distance = calculate_distance(movements)
    print(distance)
    
# Run the main function
if __name__ == "__main__":
    main()