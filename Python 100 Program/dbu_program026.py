#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 26 :

# Define a function which can compute the sum of two numbers.

# Hints:
# Define a function with two numbers as arguments.
# You can compute the sum in the function and return the value.


def main():

    def fun(num1, num2):
        return num1 + num2

    print fun(int(raw_input('Enter number1: ')),
              int(raw_input('Enter number2: ')))

if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print 'Check Value'
