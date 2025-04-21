# User thru input and chake number is palindrome or not
number = int(input("Enter Number : "))
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
# Chake Number and Reverse Number
if original == reverse:
    print("Number is Palindrome")
else:
    print("Number is Not Palindrome")
# Complet
print("Complet")