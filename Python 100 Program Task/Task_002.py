# program002 :

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


# all logic should be in side main method only


# Define Main Function
def main(fact_number):
    
    # Check if the Factorial Number is 0
    
    if fact_number == 0:
        return 1
    
    copy_fact_number = fact_number
    # Return the Factorial Number
    for i in range(copy_fact_number - 1, 0, -1):
        fact_number *= i
    return fact_number

# Number Taken from User
fact_number = int (input('Enter Factorial Number:'))

# Main method Call and out put store in result veriabel
result = main(fact_number)

# Print The result 
print("Output is : " , result)