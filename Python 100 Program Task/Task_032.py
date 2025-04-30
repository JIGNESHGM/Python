# program 32 :

# Define a function that can accept an integer number as input
# and print the "It is an even number" if the number is even,
# otherwise print "It is an odd number".

# Hints:
# Use % operator to check if a number is even or odd.

# Funcation Create chake number is even or not 
def chake_number_even_odd(num):
    # Condition check number is even or not and return True or false 
    if num % 2 == 0:
        return True
    else:
        return False
    
# Main function
def main():
    # Input from user 
    num = int(input("Enter Number: "))
    # Function call and check number is even or not 
    if chake_number_even_odd(num):
        print("{0} It is an even number".format(num))
    else:
        print("{0} It is an odd number".format(num))

# Check main function
if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print('Check Value')