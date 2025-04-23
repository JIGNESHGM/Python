#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 30 :

# Define a function that can accept two strings
# as input and concatenate them and then print it in console.

# Hints:
# Use + to concatenate the strings


def main():

    def function(string1, string2):
        return string1 + string2

    print function(raw_input('Enter first name:'),
                   raw_input('Enter last name: '))

if __name__ == '__main__':
    main()
