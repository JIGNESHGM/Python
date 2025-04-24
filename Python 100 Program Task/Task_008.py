# program008 :

# Write a program that accepts a comma separated sequence of words as
# input and prints the words in a comma-separated sequence after sorting
# them alphabetically.

# Suppose the following input is supplied to the program:
# without,hello,bag,world

# Then, the output should be:
# bag,hello,without,world

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


# Main Funcation Declaration Withe Logic

def main(items):
    
    # Sorting the list of items
    items.sort()
    
    # Joining the sorted list into a comma-separated string
    return ','.join(items)

# User Thru Items Recived 

if __name__ == '__main__':
    #
    # Try to get the input from the user
    
    try:
        # Taking input from the user
        
        item = str(input("Enter the items separated by commas: "))
        
        # Splitting the input string into a list of items
        items = item.split(',')
        # Calling the main function and printing the result
        result = main(items)
        
        print(result)
    except ValueError:
        # Handling ValueError if the input is not valid
        print('Check Value')