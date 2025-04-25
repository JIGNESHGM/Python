# program 20 :

# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield


# Funcation to check if a number is divisible by 7 or not
def is_divisible_by_7(num):
    if num % 7 == 0:
        return True
    else:
        return False
    
# Generator function to yield numbers divisible by 7
def divisible_by_7_generator(n):
    for num in range(0, n + 1):
        if is_divisible_by_7(num):
            yield num
            
# Main function to test the generator
def main():
    n = int(input("Enter a number: "))
    print(f"Numbers divisible by 7 between 0 and {n}:")
    for num in divisible_by_7_generator(n):
        print(num, end=" ")

# Call the main function
if __name__ == "__main__":
    main()