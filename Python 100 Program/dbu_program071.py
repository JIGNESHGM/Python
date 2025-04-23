#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


def main(exp):

    print eval(exp)

if __name__ == '__main__':
    try:
        exp = raw_input()
        main(exp)
    except(ValueError, SyntaxError, NameError):
        print 'Check Value or/and Expression'
