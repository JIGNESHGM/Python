#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 42 :

# With a given tuple (1,2,3,4,5,6,7,8,9,10),
# write a program to print the first half values
# in one line and the last half values in one line.

# Hints:
# Use [n1:n2] notation to get a slice from a tuple.


def main(num1, num2):

    lis = list()
    if num1 < num2:
        for cnt in range(num1, num2 + 1):
            lis.append(cnt)
        tup = tuple(lis)

        print tup[:(num2 / 2)]
        print tup[(num2 / 2):]

    else:
        print 'Ending range must be greater than starting range'


if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter starting range: '))
        num2 = int(raw_input('Enter ending range: '))
        main(num1, num2)
    except ValueError:
        print 'Check Value'
