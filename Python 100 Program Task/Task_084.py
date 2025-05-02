# program 84:

# Please write a program to shuffle
# and print the list [3,6,7,8].

# Hints:
# Use shuffle() function to shuffle a list.

# Function to shuffle and print the list [3, 6, 7, 8]
import random

def shuffle_list(input_list):
    # Shuffle the input list
    random.shuffle(input_list)
    return input_list

# Main function to execute the program
def main():
    # Define the list to be shuffled
    input_values = input("Enter comma-separated values: ")
    input_list = [int(value.strip()) for value in input_values.split(",")]
    
    # Shuffle the list and print the result
    shuffled_list = shuffle_list(input_list)
    print(f"Shuffled list: {shuffled_list}")
    
# Call the main function to run the program
if __name__ == "__main__":
    main()