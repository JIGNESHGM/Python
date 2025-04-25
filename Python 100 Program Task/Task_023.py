# program 23 :

# Write a method which can calculate square value of number

# Hints:
# Using the ** operator

# Function to calculate square
def calculate_square(num):
    return num ** 2

# Main function declaration
def main():
    num = int(input("Enter a number to find its square: "))
    print(f"The square of {num} is {calculate_square(num)}")

if __name__ == "__main__":
    main()