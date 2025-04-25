# program 19 :

# You are required to write a program to sort the
# (name, age, height) tuples by ascending order
# where name is string, age and height are numbers.
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'),
# ('Json', '21', '85'), ('Tom', '19', '80')]

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


# Funcation creare tuple
def create_tuple():
    # Create an empty list to store the tuples
    tuples_list = []
    
    # Loop to take input from the user
    while True:
        # Take input from the user
        user_input = input("Enter name, age, height (or 'stop' to finish): ")
        
        # Check if the user wants to stop
        if user_input.lower() == 'stop':
            break
        
        # Split the input string into a tuple
        name, age, height = user_input.split(',')
        
        # Append the tuple to the list
        tuples_list.append((name, age, height))
    
    return tuples_list

# Function to sort the tuples
def sort_tuples(tuples_list):
    # Sort the list of tuples based on the criteria
    sorted_list = sorted(tuples_list, key=lambda x: (x[0], int(x[1]), int(x[2])))
    
    return sorted_list

# Main function
def main():
    # Create tuples
    tuples_list = create_tuple()
    
    # Sort the tuples
    sorted_list = sort_tuples(tuples_list)
    
    # Print the sorted list
    print(sorted_list)


# Call the main function
if __name__ == "__main__":
    main()