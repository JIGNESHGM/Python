#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 48 :

# Write a program which can filter() to make a list
# whose elements are even number between 1 and 20 (both included).

# Hints:
# Use filter() to filter elements of a list.
# Use lambda to define anonymous functions.


def main(num1, num2):

    if num1 < num2:
        ans = filter(lambda num: num % 2 == 0, range(num1, num2 + 1))
        print ans

    else:
        print 'Ending range must be greater than starting range'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter starting range: '))
        num2 = int(raw_input('Enter ending range: '))
        main(num1, num2)
    except ValueError:
        print 'Check Value'
