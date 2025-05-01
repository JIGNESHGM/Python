# program 53 :

# Define a class named Rectangle which can be
# constructed by a length and width.
# The Rectangle class has a method which can compute the area.

# Hints:
# Use def methodName(self) to define a method.

# Class to represent a Rectangle
class Rectangle:
    # Constructor to initialize the length and width of the rectangle
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to compute the area of the rectangle
    def compute_area(self):
        return self.length * self.width
    
# Main function to test the Rectangle class
def main():
    # Prompt the user to enter the length and width of the rectangle
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Create an instance of the Rectangle class
    rectangle = Rectangle(length, width)
    
    # Compute and print the area of the rectangle
    area = rectangle.compute_area()
    print("The area of the rectangle with length", length, "and width", width, "is:", area)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()