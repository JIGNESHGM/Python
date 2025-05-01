# program 73:

# Please write a binary search function
# which searches an item in a sorted list
# The function should return
# the index of element to be searched in the list

# Hints:
# Use if/elif to deal with conditions.

def binary_search(sorted_list, target):
    """
    Perform binary search on a sorted list to find the target element.
    
    Args:
        sorted_list: A list of sorted elements
        target: The element to search for
        
    Returns:
        The index of the target element if found, otherwise -1
    """
    left, right = 0, len(sorted_list) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Get user input
user_input = input("Enter comma-separated sorted numbers: ")
try:
    sorted_list = [int(x.strip()) for x in user_input.split(',')]
    target = int(input("Enter the number to search for: "))
    
    # Verify the list is sorted
    if sorted_list != sorted(sorted_list):
        print("Warning: The list you entered is not sorted. Binary search requires a sorted list.")
    
    # Perform the search
    result = binary_search(sorted_list, target)
    
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the list.")
except ValueError:
    print("Invalid input. Please enter numbers only.")