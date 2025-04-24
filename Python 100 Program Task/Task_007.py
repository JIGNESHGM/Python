# program007:

# Write a program which takes 2 digits, X,Y as input and
# generates a 2-dimensional array. The element value in the i-th row and
# j-th column of the array should be i*j.

# Note: i=0,1.., X-1; j=0,1,Y-1.

# Example
# Suppose the following inputs are given to the

# program:
# 3,5

# Then, the output of the program should be:
#[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# Hints:
# Note: In case of input data being supplied to the
# question, it should be assumed to be a console input
# in a comma-separated form.


# Main function Declaration

def main(row, col):
    # List comprehension to create a 2D array
    arr = []
    
    # Column loop
    for i in range(row):
        
        # and appending it to the array
        row_data = []
        
        for j in range(col):
            row_data.append(i * j)
        arr.append(row_data)
    # Returning the 2D array
    return arr

# Main function Execution
if __name__ == '__main__':
    try:
        # Taking input from user
        row = int(input('Enter no of Rows: '))
        col = int(input('Enter no of Cols: '))
        
        # Printing the 2D array
        print(main(row, col))
    
    # Handling ValueError
    except ValueError:
        print('Check value')

