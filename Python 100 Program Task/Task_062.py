# program 62 :


# Write a program to read an ASCII string and
# to convert it to a unicode string encoded by utf-8.

# Hints:
# Use unicode() function to convert.


# Function to convert an ASCII string to a unicode string encoded by utf-8
def convert_ascii_to_unicode(ascii_string):
    # Convert the ASCII string to a unicode string using utf-8 encoding
    unicode_string = ascii_string.encode("utf-8")
    
    # Return the unicode string
    return unicode_string

# Main function to test the convert_ascii_to_unicode function
def main():
    # Define an ASCII string
    ascii_string = "hello world"
    
    # Call the function to convert the ASCII string to a unicode string
    unicode_string = convert_ascii_to_unicode(ascii_string)
    
    # Print the unicode string
    print(unicode_string)
    
# Call the main function to execute the program
if __name__ == "__main__":
    main()