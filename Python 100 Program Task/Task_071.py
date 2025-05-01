# program 71:

# Please write a program which accepts
# basic mathematic expression from console
# and print the evaluation result.

# Example:
# If the following string is given as input to the program:

# 35+3

# Then, the output of the program should be:

# 38

# Hints:
# Use eval() to evaluate an expression.

def main():
    try:
        expression = input("Enter a basic mathematical expression (e.g., 35+3): ")
        result = eval(expression)
        print("Result:", result)
    except Exception as e:
        print("Invalid expression. Error:", e)

if __name__ == "__main__":
    main()
