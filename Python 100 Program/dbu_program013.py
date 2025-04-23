#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 13 :

# Write a program that accepts a sentence and
# calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def main(string):

    ans = {"DIGITS": 0, "LETTERS": 0}
    for cnt in string:
        if cnt.isdigit():
            ans["DIGITS"] += 1
        elif cnt.isalpha():
            ans["LETTERS"] += 1
        else:
            pass
    print "LETTERS", ans["LETTERS"]
    print "DIGITS", ans["DIGITS"]

if __name__ == '__main__':

    try:
        string = raw_input()
        main(string)
    except ValueError:
        print 'Check Input'
