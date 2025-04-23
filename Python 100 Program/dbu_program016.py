#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 16 :

# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def main(values):

    return [num for num in values if int(num) % 2 != 0]

if __name__ == '__main__':
    try:
        values = [int(num) for num in raw_input("enter no:").split(",")]
        print main(values)
    except ValueError:
        print 'Check Value'
