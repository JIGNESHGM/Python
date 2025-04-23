# program004:

# Write a program which accepts a sequence of comma-separated numbers
# from console and generate a list and a tuple which contains every number.

# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98

# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# tuple() method can convert list to tuple

# all logic should be in side main method only


# Defind Main Function

def main(num):
    
    # List Veriabel Defind 
    
    NumberList = num.split(",")
    
    # Tuple Veriabel Defind
    NumberTuple = tuple(NumberList)
    
    # Print List
    print(NumberList)
    
    # Print Tuple
    print(NumberTuple)

# User Tthru input 

num = input('Enter numbers (in Integer) : ')

# Call Main Function
main(num)
# End of Program