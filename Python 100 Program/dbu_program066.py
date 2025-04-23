#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 66:

# The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

# Please write a program to compute the value
# of f(n) with a given n input by console.

# Example:
# If the following n is given as input to the program:

# 7

# Then, the output of the program should be:

# 13

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Hints:
# We can define recursive function in Python.


def main(num):

    def fun(num):

        if num == 0:
            return 0
        elif num == 1:
            return 1
        else:
            return fun(num - 1) + fun(num - 2)
    print fun(num)

if __name__ == '__main__':
    try:
        num = int(raw_input('Enter any number: '))
        main(num)
    except ValueError:
        print 'Check Value'
