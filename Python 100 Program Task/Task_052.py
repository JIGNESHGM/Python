# program 52 :

# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

# Hints:
# Use def methodName(self) to define a method.

# Class to represent a Circle
class Circle:
    # Constructor to initialize the radius of the circle
    def __init__(self, radius):
        self.radius = radius

    # Method to compute the area of the circle
    def compute_area(self):
        return 3.14 * (self.radius ** 2)
    
# Main function to test the Circle class
def main():
    # Prompt the user to enter the radius of the circle
    radius = float(input("Enter the radius of the circle: "))
    
    # Create an instance of the Circle class
    circle = Circle(radius)
    
    # Compute and print the area of the circle
    area = circle.compute_area()
    print("The area of the circle with radius", radius, "is:", area)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()