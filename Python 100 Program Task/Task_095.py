# program 95:

# Define a class Person and its two child classes: Male and Female. All
# classes have a method "getGender" which can print "Male" for Male class
# and "Female" for Female class.

# Hints:
# Use Subclass(Parentclass) to define a child class.

# Function to define the Person class and its child classes
class Person:
    def getGender(self):
        return "Person"

class Male(Person):
    def getGender(self):
        return "Male"

class Female(Person):
    def getGender(self):
        return "Female"
    
# Main function to execute the program
def main():
    male = Male()
    female = Female()
    print("Male class getGender():", male.getGender())
    print("Female class getGender():", female.getGender())

# Call the main function to run the program
if __name__ == "__main__":
    main()