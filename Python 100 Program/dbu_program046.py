#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 46 :

# Write a program which can map() to make a list whose elements
# are square of elements in [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.


def main(num1, num2):

    if num1 < num2:
        lis = list()
        for cnt in range(num1, num2 + 1):
            lis.append(cnt)

        square = map(lambda num: num ** 2, lis)

        print square

    else:
        print 'Ending range must be greater than starting range'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter starting range: '))
        num2 = int(raw_input('Enter ending range: '))
        main(num1, num2)
    except ValueError:
        print 'Check Value'
