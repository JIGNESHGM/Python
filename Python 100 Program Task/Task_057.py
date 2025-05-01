# program 57 :


# Define a custom exception class which takes a string message as attribute.

# Hints:
# To define a custom exception, we need to define a class inherited from
# Exception.

# Custom exception class inheriting from Exception
class CustomException(Exception):
    def __init__(self, message):
        # Initialize the exception with a message
        self.message = message

    def __str__(self):
        # Return the string representation of the exception
        return f"CustomException: {self.message}"
    
# Main function to demonstrate the usage of the custom exception
def main():
    try:
        # Raise the custom exception with a message
        raise CustomException("This is a custom exception message.")
    except CustomException as e:
        # Handle the custom exception and print the error message
        print(e)
        # You can also access the message attribute directly
        print("Accessing message directly:", e.message)
        # You can also use the str() method to get the string representation
        print("String representation:", str(e))
        # You can also use the __str__ method directly
        print("Using __str__ method:", e.__str__())
        # You can also use the vars() function to get the attributes of the exception
        print("Attributes of the exception:", vars(e))
        # You can also use the __dict__ attribute to get the attributes of the exception
        print("Attributes of the exception using __dict__:", e.__dict__)
        # You can also use the type() function to get the type of the exception 
        print("Type of the exception:", type(e))
        
# Program entry point
if __name__ == "__main__":
    main()