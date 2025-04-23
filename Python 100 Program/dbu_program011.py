#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 11 :

# Write a program which accepts a sequence of comma
# separated 4 digit binary numbers as its input and then
# check whether they are divisible by 5 or not. The numbers
# that are divisible by 5 are to be printed in a comma
# separated sequence.

# Example:
# 0100,0011,1010,1001

# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def main(items):

    value = []

    for tup in items:
        ans = int(tup, 2)
        if not ans % 5:
            value.append(tup)

    return ','.join(value)

if __name__ == '__main__':
    try:
        items = [cnt for cnt in raw_input('Enter Value: ').split(',')]
        print main(items)
    except ValueError:
        print 'Check Input'
