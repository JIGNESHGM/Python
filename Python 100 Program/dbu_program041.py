#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 41 :

# Define a function which can generate and print
# a tuple where the value are square of
# numbers between 1 and 20 (both included).

# Hints:
# Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.
# Use tuple() to get a tuple from a list.


def main(num1, num2):

    lis = list()
    if num1 < num2:
        for cnt in range(num1, num2 + 1):
            lis.append(cnt ** 2)
        print tuple(lis)

    else:
        print 'Ending range must be greater than starting range'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter starting range: '))
        num2 = int(raw_input('Enter ending range: '))
        main(num1, num2)
    except ValueError:
        print 'check value'
