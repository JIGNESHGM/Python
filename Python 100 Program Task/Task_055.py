# program 55 :

# Please raise a RuntimeError exception.

# Hints:
# Use raise() to raise an exception.

# Function to raise a RuntimeError exception
def raise_runtime_error():
    raise RuntimeError("This is a RuntimeError exception.")

# Main function to test the raise_runtime_error function
def main():
    try:
        # Call the function that raises a RuntimeError
        raise_runtime_error()
    except RuntimeError as e:
        # Handle the exception and print the error message
        print("Caught an exception:", e)
        
# Call the main function to execute the program
if __name__ == "__main__":
    main()