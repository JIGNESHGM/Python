# program005:

# Define a class which has at least two methods:
# get_input_string: to get a string from console input
# print_uppercase_string: to print the string in upper case.
# Also please include a simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

# Class Declaration
class StringProcessor(object):

    # Constructor
    def __init__(self):
        self.input_string = ""

    # Get String from Console Input
    def get_input_string(self):
        # Get String from Console Input
        self.input_string = str(input('Enter a string: '))

    # Print String in Upper Case
    def print_uppercase_string(self):
        # Return String in Upper Case
        return self.input_string.upper()

    # Test Function
    def test_function(self):
        # Return Test Function Result
        return 'Test function is working properly... OK'


# Main Function Declaration
def main():
    # Create Object of Class
    string_processor = StringProcessor()
    # Call Class Methods
    print(string_processor.test_function())  # Test function first
    string_processor.get_input_string()      # Get string from user
    print(string_processor.print_uppercase_string())  # Print string in uppercase


# Main Function Call
if __name__ == '__main__':
    main()
