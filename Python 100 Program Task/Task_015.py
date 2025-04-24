# program 15 :

# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


# Function to calculate the value of a+aa+aaa+aaaa

def calculate_value(a):
    
    # Calculate the value of a+aa+aaa+aaaa
    result = 0
    for i in range(1, 5):
        result += int(a * i)
    return result

# Main Funcation

def main():
    
    # Input from user
    a = input("Enter a digit: ")
    
    # Call the function to calculate the value
    result = calculate_value(a)
    
    # Print the result
    print(f"The value of {a} + {a*2} + {a*3} + {a*4} is: {result}")
    
    
# Call the main function
if __name__ == "__main__":
    main()