# program 31 :

# Define a function that can accept two strings as input
# and print the string with maximum length in console.
# If two strings have the same length, then the function
# should print all strings line by line.

# Hints:
# Use len() function to get the length of a string

# Funcation to compare two strings and print the longer one
def compare_strings(str1, str2):
    # Check the length of both strings
    len_str1 = len(str1)
    len_str2 = len(str2)

    # Compare lengths and print accordingly
    if len_str1 > len_str2:
        print(f"The longer string is: {str1}")
    elif len_str2 > len_str1:
        print(f"The longer string is: {str2}")
    else:
        print("Both strings are of equal length:")
        print(str1)
        print(str2)
        
# Main Funcation Delcaration
def main():
    # Input two strings from the user
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")

    # Call the function to compare and print the strings
    compare_strings(string1, string2)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()