# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords
# and will check them according to the above criteria.
# Passwords that match the criteria are to be printed,
# each separated by a comma.

# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.\
    
# Function to check password validity based on specific criteria
def check_password_validity(password):

    # Check if password length is between 6 and 12 characters
    if len(password) < 6 or len(password) > 12:
        return False, "Password length should be between 6 and 12"

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False, "Password should contain at least 1 lowercase letter [a-z]"

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False, "Password should contain at least 1 uppercase letter [A-Z]"

    # Check if the password contains at least one digit
    if not any(char.isdigit() for char in password):
        return False, "Password should contain at least 1 digit [0-9]"

    # Check if the password contains at least one special character from [$#@]
    if not any(char in ['$','#','@'] for char in password):
        return False, "Password should contain at least 1 special character from [$#@]"

    # If all conditions are satisfied, return True
    return True, "Password is valid"

# Main function to handle user input and check passwords
def main():
    try:
        # Prompt user to enter passwords separated by commas
        passwords_input = input("Enter passwords separated by commas: ").strip()

        # If input is empty, show message and exit
        if not passwords_input:
            print("No input received. Please enter at least one password.")
            return

        # Split the input string into individual passwords and remove extra spaces
        password_list = [password.strip() for password in passwords_input.split(',') if password.strip()]

        # Create a list to store valid passwords
        valid_passwords = []

        # Loop through each password to check if it's valid
        for password in password_list:
            # Call the function to validate password
            is_valid, message = check_password_validity(password)

            # If valid, add to the list of valid passwords
            if is_valid:
                valid_passwords.append(password)
            else:
                # If invalid, print error message with reason
                print(f" '{password}': {message}")

        # If any valid passwords found, print them
        if valid_passwords:
            print("\n Valid password(s):")
            print(", ".join(valid_passwords))  # Join the list with commas
        else:
            # If no valid passwords found
            print("\n No valid passwords found.")

    # Catch and print any unexpected errors
    except Exception as e:
        print(f" An error occurred: {e}")

# Call the main function to execute the program
if __name__ == "__main__":
    main()