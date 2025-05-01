# program 44 :

# Write a program which accepts a string as input to print "Yes"
# if the string is "yes" or "YES" or "Yes", otherwise print "No".

# Hints:
# Use if statement to judge condition.

# Function to check if the input string is "yes" in any case
def is_yes(string):
    # Convert the string to lowercase and check if it is "yes"
    return string.lower() == "yes"

# Main function to get user input and print the result
def main():
    # Get user input
    string = input("Enter string: ")
    
    # Check if the input string is "yes" in any case and print the result
    if is_yes(string):
        print("Yes")
    else:
        print("No")
        
# Call the main function to execute the program
if __name__ == "__main__":
    main()