# program 56 :

# Write a function to compute 5/0 and use try/except to catch the exceptions.

# Hints:
# Use try/except to catch exceptions.

# Function to compute 5 divided by 0 and handle the exception
def compute_division():
    try:
        # Attempt to divide 5 by 0
        result = 5 / 0
    except ZeroDivisionError as e:
        # Handle the ZeroDivisionError exception
        print("Caught an exception:", e)
        return None
    return result

# Main function to test the compute_division function
def main():
    
    # Call the function that computes 5/0
    result = compute_division()
    if result is not None:
        print("Result:", result)
    else:
        print("No result due to exception.")
        
# Call the main function to execute the program
if __name__ == "__main__":
    main()