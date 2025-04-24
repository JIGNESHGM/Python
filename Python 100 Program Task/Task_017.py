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

def net_amount():
    # Initialize the net amount to 0
    net_amount = 0

    while True:
        try:
            # Display options to the user
            print("\nSelect an option:")
            print("1. Deposit")
            print("2. Withdrawal")
            print("3. Exit")
            
            # Get the user's choice
            choice = input("Enter your choice (1/2/3): ").strip()

            # Handle the user's choice
            if choice == '1':  # Deposit
                amount = input("Enter deposit amount: ").strip()
                if not amount.isdigit() or int(amount) <= 0:
                    print("Invalid amount. Please enter a positive number.")
                    continue
                net_amount += int(amount)
                print(f"Deposited: {amount}. Current Net Amount: {net_amount}")
            elif choice == '2':  # Withdrawal
                amount = input("Enter withdrawal amount: ").strip()
                if not amount.isdigit() or int(amount) <= 0:
                    print("Invalid amount. Please enter a positive number.")
                    continue
                if int(amount) > net_amount:
                    print("Insufficient balance. Cannot withdraw more than the current net amount.")
                    continue
                net_amount -= int(amount)
                print(f"Withdrawn: {amount}. Current Net Amount: {net_amount}")
            elif choice == '3':  # Exit
                print(f"Final Net Amount: {net_amount}")
                break
            else:
                print("Invalid choice. Please select 1, 2, or 3.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

# Create a main function to call the net_amount function
def main():
    net_amount()

# Call the main function
if __name__ == "__main__":
    main()