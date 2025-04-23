#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 14 :

# Write a program that accepts a sentence and
# calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def main(string):

    ans = {"upperCase": 0, "lowerCase": 0}
    for cnt in string:
        if cnt.isupper():
            ans["upperCase"] += 1
        elif cnt.islower():
            ans["lowerCase"] += 1
        else:
            pass
    print "UPPER CASE", ans["upperCase"]
    print "LOWER CASE", ans["lowerCase"]

if __name__ == '__main__':

    try:
        string = raw_input()
        main(string)
    except ValueError:
        print 'Check Input'
