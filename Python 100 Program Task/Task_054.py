# program 54 :

# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape
# where Shape's area is 0 by default.

# Hints:
# To override a method in super class,
# we can define a method with the same name in the super class.

# Class to represent a generic Shape
class Shape:
    # Constructor to initialize the shape (default area is 0)
    def __init__(self):
        self.area_value = 0

    # Method to compute the area of the shape (default is 0)
    def area(self):
        return self.area_value
    
# Class to represent a Square, inheriting from Shape
class Square(Shape):
    # Constructor to initialize the length of the square
    def __init__(self, length):
        super().__init__()  # Call the constructor of the parent class
        self.length = length

    # Method to compute the area of the square
    def area(self):
        self.area_value = self.length ** 2  # Area of square = length^2
        return self.area_value
    
# Main function to test the Shape and Square classes
def main():
    # Create an instance of the Shape class
    shape = Shape()
    print("Area of Shape:", shape.area())  # Should print 0

    # Prompt the user to enter the length of the square
    length = float(input("Enter the length of the square: "))

    # Create an instance of the Square class
    square = Square(length)
    
    # Compute and print the area of the square
    area = square.area()
    print("Area of Square with length", length, "is:", area)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()
    