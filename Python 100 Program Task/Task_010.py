# program010 :

# Write a program that accepts a sequence of whitespace separated words as
# input and prints the words after removing all duplicate words and
# sorting them alphanumerically.

# Suppose the following input is supplied to the
# program:
# hello world and practice makes perfect and hello world again

# Then, the output should be:
# again and hello makes perfect practice world

# Hints:
# In case of input data being supplied to the question, it
# should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then
# use sorted() to sort the data.


# Main Function Declaration and Logic

def main(sentence):
    # Split the sentence into words
    words = list(set(sentence.split(" ")))
    
    # Sort the words alphanumerically
    words.sort()
    
    # Join the words back into a single string
    return " ".join(words)

# Main Function Call
if __name__ == "__main__":
    try:
        # Input from the user
        sentence = input("Enter a sentence: ")
        
        # Calling the main function
        result = main(sentence)
        
        # Print the result
        print(result)
    
    # Handle exceptions
    except ValueError:
        print("Check Input")
    except Exception as e:
        print(f"An error occurred: {e}")