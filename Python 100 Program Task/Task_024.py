# program 24 :

# Python has many built-in functions, and if you do not know how to use it,
# you can read document online or find some books.
# But Python has a built-in document function for every built-in functions.
# Please write a program to print some Python built-in functions documents,
# such as abs(), int(), raw_input()
# And add document for your own function

# Hints:
# The built - in document method is __doc__

# Function to print the documentation of built-in functions
def print_builtin_docs():
    # list of bilt-in function to print documentation
    builtin_functions = [abs, int, input]
    # iterate through the list of functions
    for func in builtin_functions:
        # print the function name and its documentation
        print(f"{func.__name__} documentation: {func.__doc__}\n")
    

# Print the documentation of built-in functions
print_builtin_docs()