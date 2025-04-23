#!/usr/bin/python
# -*- coding: utf-8 -*-

# program008 :

# Write a program that accepts a comma separated sequence of words as
# input and prints the words in a comma-separated sequence after sorting
# them alphabetically.

# Suppose the following input is supplied to the program:
# without,hello,bag,world

# Then, the output should be:
# bag,hello,without,world

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def main(items):

    items.sort()
    return ','.join(items)

if __name__ == '__main__':
    try:
        items = [cnt for cnt in raw_input().split(',')]
        print main(items)
    except ValueError:
        print 'Check Value'
