def is_palindrome(number):
    # Reverse Number
    reverse = 0
    # Original Number
    original = number
    # Loop for Reverse Number
    while number > 0:
        # Last Digit
        digit = number % 10
        # Reverse Number
        reverse = reverse * 10 + digit
        # Number Divide by 10
        number = number // 10
    # Check Number and Reverse Number
    return original == reverse

def main():
    # User input
    number = int(input("Enter Number: "))
    # Check if the number is a palindrome
    if is_palindrome(number):
        print("Number is Palindrome")
    else:
        print("Number is Not Palindrome")
    # Complete
    print("Complete")

if __name__ == "__main__":
    main()