# program 30 :

# Define a function that can accept two strings
# as input and concatenate them and then print it in console.

# Hints:
# Use + to concatenate the strings

# Function Create
def concatenate_strings(str1, str2):
    return str1 + " " + str2
    
# Main Function
def main():
    # Input from user
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")
    
    # Call the function to concatenate and print
    result = concatenate_strings(string1, string2)
    
    #Print Result 
    print("Your String Concatenate after : \n {0}".format(result))
    
# Call the main function
if __name__ == "__main__":
    main()