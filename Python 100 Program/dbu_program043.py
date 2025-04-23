#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 43 :

# Write a program to generate and print another
# tuple whose values are even numbers
# in the given tuple (1,2,3,4,5,6,7,8,9,10).

# Hints:
# Use "for" to iterate the tuple
# Use tuple() to generate a tuple from a list.


def main(num1, num2):

    if num1 < num2:
        tup = (range(num1, num2 + 1))
        lis = list()
        for cnt in tup:
            if cnt % 2 == 0:
                lis.append(cnt)

        tp = tuple(lis)
        return tp

    else:
        print 'Ending range must be greater than starting range'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter starting range: '))
        num2 = int(raw_input('Enter ending range: '))
        print main(num1, num2)
    except ValueError:
        print 'Check Value'
