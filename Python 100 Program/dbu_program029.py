#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 29 :

# Define a function that can receive
# two integral numbers in string form
# and compute their sum and then print it in console.

# Hints:
# Use int() to convert a string to integer.


def main():

    def function(num1, num2):
        return int(num1) + int(num2)

    print function(raw_input('Enter num1: '),
                   raw_input('Enter num2: '))

if __name__ == '__main__':
    main()
