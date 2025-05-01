# program 64:

# Write a program to compute 1/2+2/3+3/4+...+n/n+1
# with a given n input by console (n>0).

# Example:
# If the following n is given as input to the program:

# 5

# Then, the output of the program should be:

# 3.55

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Hints:
# Use float() to convert an integer to a float

# Function to compute the sum of the series 1/2 + 2/3 + ... + n/(n+1)
def compute_series_sum(n):
    # Initialize the sum to 0
    total_sum = 0.0
    # Loop through the range from 1 to n (inclusive)
    for i in range(1, n + 1):
        # Add the term i/(i+1) to the total sum
        total_sum += i / (i + 1)
    return total_sum

# Main function to test the compute_series_sum function
def main():
    # Input n from the user
    n = int(input("Enter a positive integer n: "))
    
    # Check if n is greater than 0
    if n > 0:
        result = compute_series_sum(n)
        print("The sum of the series is:", result)
    else:
        print("Please enter a positive integer greater than 0.")
        

# Call the main function to execute the program
if __name__ == "__main__":
    main()