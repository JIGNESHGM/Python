# program 50 :
# Define a class named American which has
# a static method called printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.

# Function create a class named American
class American:
    # Static method to print nationality
    @staticmethod
    def printNationality():
        print("American")
        
    
# Main function to test the American class
def main():
    # Create an instance of the American class
    american_instance = American()
    
    # Call the static method to
    american_instance.printNationality()
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()    