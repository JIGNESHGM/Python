# program 59 :

# Assuming that we have some email addresses
# in the "username@companyname.com" format,
# please write program to print the company name of a given email address.
# Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# john@google.com

# Then, the output of the program should be:

# google

# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# Hints:
# Use \w to match letters.

# Function to extract the company name from an email address
def extract_company_name(email):
    # Split the email address at the '@' symbol and return the second part (company name without domain)
    return email.split('@')[1].split('.')[0]

# Main function to test the extract_company_name function
def main():
    # Input email address from the user
    email = input("Enter an email address (username@companyname.com): ")
    
    company_name = extract_company_name(email)
    print("Company name:", company_name)


# Call the main function to execute the program
if __name__ == "__main__":
    main()s