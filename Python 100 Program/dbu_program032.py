#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 32 :

# Define a function that can accept an integer number as input
# and print the "It is an even number" if the number is even,
# otherwise print "It is an odd number".

# Hints:
# Use % operator to check if a number is even or odd.


def main():

    def function(num):
        if num % 2 == 0:
            return 'It is an even number'
        else:
            return 'It is an odd number'

    print function(int(raw_input('Enter Number: ')))

if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print 'Check Value'
