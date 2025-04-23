#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 90:

# By using list comprehension, please write a program generate a 3*5*8 3D
# array whose each element is 0.

# Hints:
# Use list comprehension to make an array.


def main(num1, num2, num3):

    array = [[['@' for col in range(num3)]
              for col in range(num2)]
             for row in range(num1)]

    return array

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter num1: '))
        num2 = int(raw_input('Enter num2: '))
        num3 = int(raw_input('Enter num3: '))
        print main(num1, num2, num3)
    except ValueError:
        print 'Check Value'
