#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 31 :

# Define a function that can accept two strings as input
# and print the string with maximum length in console.
# If two strings have the same length, then the function
# should print all strings line by line.

# Hints:
# Use len() function to get the length of a string


def main(s1, s2):

    def function(string1, string2):
        len1 = len(string1)
        len2 = len(string2)

        if(len1 > len2):
            print string1
        elif(len2 > len1):
            print string2
        else:
            print string1
            print string2

    function(s1, s2)

if __name__ == '__main__':
    s1 = raw_input('Enter string1: ')
    s2 = raw_input('Enter string2: ')

    main(s1, s2)
