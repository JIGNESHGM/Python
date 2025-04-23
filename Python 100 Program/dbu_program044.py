#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 44 :

# Write a program which accepts a string as input to print "Yes"
# if the string is "yes" or "YES" or "Yes", otherwise print "No".

# Hints:
# Use if statement to judge condition.


def main(string):

    if string == 'yes' or string == 'YES' or string == 'Yes':
        print 'Yes'
    else:
        print 'No'

if __name__ == '__main__':
    string = raw_input('Enter string: ')
    main(string)
