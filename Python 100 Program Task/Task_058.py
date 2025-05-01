# program 58 :

# Assuming that we have some email addresses
# in the "username@companyname.com" format,
# please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# john@google.com

# Then, the output of the program should be:

# john

# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# Hints:
# Use \w to match letters.

# Function to extract the username from an email address
def extract_username(email):
    # Split the email address at the '@' symbol and return the first part
    return email.split('@')[0]

# Main function to test the extract_username function
def main():
    # Input email address from the user
    email = input("Enter an email address (username@companyname.com): ")

    username = extract_username(email)
    print("Username:", username)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()