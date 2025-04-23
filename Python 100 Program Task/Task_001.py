# program001 :

# Define the program name
# Write a program which will find all such numbers which are
# divisible by 7 but are not a multiple of 5, between 2000
# and 3200 (both included).

# The numbers obtained should be printed in a comma-separated
# sequence on a single line.

# Hints:
# Consider use range(#begin, #end) method

# all logic should be in side main method only



# Defind Main Function

def main(start, end):
    
    # defind List Veriabel
    defind_arr_number_list = []
    
    # Looping for the range
    
    for i in range(start, end):
        
        #Chake The condition Number id divisible by 7 and not a multiple of 5
        if(i % 7 == 0) and (i % 5 != 0):
            
            # Append the number in the list
            defind_arr_number_list.append(str(i))
    # Return the list
    return defind_arr_number_list

# Main Function 

start = int (input('Enter Number Start:'))
end = int (input('Enter Number End:'))

# Funcation Call 
result = main(start, end)

# Print the result
print("Output is : " + ','.join(result))