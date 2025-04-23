#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 24 :

# Python has many built-in functions, and if you do not know how to use it,
# you can read document online or find some books.
# But Python has a built-in document function for every built-in functions.
# Please write a program to print some Python built-in functions documents,
# such as abs(), int(), raw_input()
# And add document for your own function

# Hints:
# The built - in document method is __doc__


def main():

    print abs.__doc__
    print int.__doc__
    print raw_input.__doc__

    def square(num):
        'It returns the square value of the input number.'
        return num ** 2

    print square(int(raw_input('Enter an integer number: ')))
    print square.__doc__

if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print 'Check Value'
