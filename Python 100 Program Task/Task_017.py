# program 17 :

# Write a program that computes the net amount of
# a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


# Function to calculate net amount based on transactions with error handling
@staticmethod
def net_amount():
   
    # Initialize the net amount to 0
    net_amount = 0

    # Start an infinite loop to keep the program running until user chooses to exit
    while True:
        try:
            # Display options to the user
            print("\nSelect an option:")
            print("1. Deposit")
            print("2. Withdrawal")
            print("3. Exit")
            
            # Get the user's choice and remove any leading/trailing whitespace
            choice = input("Enter your choice (1/2/3): ").strip()

            # Handle the user's choice
            if choice == '1':  # Deposit option selected
                # Get the deposit amount from user and strip whitespace
                amount = input("Enter deposit amount: ").strip()
                
                # Validate the input: must be digits only and positive
                if not amount.isdigit() or int(amount) <= 0:
                    print("Invalid amount. Please enter a positive number.")
                    continue  # Skip rest of loop and start over
                
                # Convert amount to integer and add to net_amount
                net_amount += int(amount)
                
                # Display transaction confirmation and current balance
                print(f"Deposited: {amount}. Current Net Amount: {net_amount}")
                
            elif choice == '2':  # Withdrawal option selected
                # Get the withdrawal amount from user and strip whitespace
                amount = input("Enter withdrawal amount: ").strip()
                
                # Validate the input: must be digits only and positive
                if not amount.isdigit() or int(amount) <= 0:
                    print("Invalid amount. Please enter a positive number.")
                    continue  # Skip rest of loop and start over
                
                # Check if sufficient balance exists for withdrawal
                if int(amount) > net_amount:
                    print("Insufficient balance. Cannot withdraw more than the current net amount.")
                    continue  # Skip rest of loop and start over
                
                # Convert amount to integer and subtract from net_amount
                net_amount -= int(amount)
                
                # Display transaction confirmation and current balance
                print(f"Withdrawn: {amount}. Current Net Amount: {net_amount}")
                
            elif choice == '3':  # Exit option selected
                # Display final balance and break out of the loop to end program
                print(f"Final Net Amount: {net_amount}")
                break
                
            else:
                # Handle invalid menu choices
                print("Invalid choice. Please select 1, 2, or 3.")
                
        except Exception as e:
            # Catch any unexpected errors and display them, then continue running
            print(f"An error occurred: {e}. Please try again.")

# Create a main function to call the net_amount function
@staticmethod
def main():
    net_amount()

# Standard Python idiom to check if this file is being run directly
if __name__ == "__main__":
    main() 