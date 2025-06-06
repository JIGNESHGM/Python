# Given a binary matrix M of size n X m. Find the maximum area of a
# rectangle formed only of 1s in the given matrix.
# Example 1:
# Input:
# n = 4, m = 4
# M[][] = {{0 1 1 0},
# {1 1 1 1},

# {1 1 1 1},
# {1 1 0 0}}
# Output: 8
# Explanation: For the above test case the
# matrix will look like
# 0 1 1 0
# 1 1 1 1
# 1 1 1 1
# 1 1 0 0
# the max size rectangle is 
# 1 1 1 1
# 1 1 1 1
# and area is 4 *2 = 8.

# Your Task: 
# Your task is to complete the function maxArea which returns the maximum
# size rectangle area in a binary-sub-matrix with all 1’s. The function takes 3
# arguments the first argument is the Matrix M[ ] [ ] and the next two are
# two integers n and m which denotes the size of the matrix M. 
# Expected Time Complexity : O(n*m)
# Expected Auixiliary Space : O(m)
# Constraints:
# 1<=n,m<=1000
# 0<=M[][]<=1

def maxArea(M, n, m):
    # Create a list to store the heights of the histogram
    height = [0] * m
    max_area = 0

    for i in range(n):
        for j in range(m):
            # Update the height of the histogram
            if M[i][j] == 0:
                height[j] = 0
            else:
                height[j] += 1
        # Calculate the maximum area for the current row's histogram
        max_area = max(max_area, largestRectangleArea(height))

    print("print max area result : {0}".format(max_area))
    return max_area

def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Append a zero to handle remaining bars in stack

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area
# Example usage
if __name__ == "__main__":
    M = [[0, 1, 1, 0],
         [1, 1, 1, 1],
         [1, 1, 1, 1],
         [1, 1, 0, 0]]
    n = len(M)
    print("print n : {0}".format(n))
    
    m = len(M[0]) if n > 0 else 0
    print("print m : {0}".format(m))
    
    # call the function and print the result
    print(maxArea(M, n, m))  # Output: 8