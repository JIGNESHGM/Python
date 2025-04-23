#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 45 :

# Write a program which can filter even numbers in
# a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

# Hints:
# Use filter() to filter some elements in a list.
# Use lambda to define anonymous functions.


def main(num1, num2):

    if num1 < num2:
        lis = list()
        for cnt in range(num1, num2 + 1):
            lis.append(cnt)

        evenNum = filter(lambda num: num % 2 == 0, lis)

        print evenNum

    else:
        print 'Ending range must be greater than starting range'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter starting range: '))
        num2 = int(raw_input('Enter ending range: '))
        main(num1, num2)
    except ValueError:
        print 'Check Value'
