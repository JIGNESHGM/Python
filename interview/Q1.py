# Given a string, find the minimum number of characters to be inserted to
# convert it to palindrome.
# For Example:
# ab: Number of insertions required is 1. bab or aba
# aa: Number of insertions required is 0. aa
# abcd: Number of insertions required is 3. dcbabcd


# You don&#39;t need to read input or print anything. Your task is to complete the
# function countMin() which takes the string str as inputs and returns the
# answer.

# Expected Time Complexity: O(N 2 ), N = |str|
# Expected Auxiliary Space: O(N 2 )

# Constraints:
# 1 ≤ |str| ≤ 10 3
# str contains only lower case alphabets.

def countMin(str):
    
    # string length calculation
    n = len(str)
    # create a 2D array to store the results of subproblems
    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if str[i] == str[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

    print("print array result : {0}".format(dp))
    return dp[0][n - 1]

# program to test the function
if __name__ == "__main__":
    print(countMin("ab"))
    print(countMin("aa"))
    print(countMin("abcd"))
    print(countMin("abcde"))