#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 28 :

# Define a function that can convert a integer
# into a string and print it in console.

# Hints:
# Use str() to convert a number to string.


def main():

    def function(num):
        return str(num)

    print function(int(raw_input('Enter any number: ')))

if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print 'Check Value'
