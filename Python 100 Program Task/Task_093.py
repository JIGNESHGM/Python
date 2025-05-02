# program 93:

# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the
# above given lists.

# Hints:
# Use set() and "&=" to do set intersection operation.

# Function to find the intersection of two lists
def find_intersection(list1, list2):
    # Convert lists to sets and find the intersection
    intersection = set(list1) & set(list2)
    return list(intersection)

# Main function to execute the program
def main():
    # Given lists
    list1 = [int(x) for x in input("Enter the first list of numbers separated by spaces: ").split()]
    list2 = [int(x) for x in input("Enter the second list of numbers separated by spaces: ").split()]
    
    # Find the intersection of the two lists
    result_list = find_intersection(list1, list2)
    
    # Print the result
    print("Intersection of the two lists:", result_list)
    
# Call the main function to run the program
if __name__ == "__main__":
    main()