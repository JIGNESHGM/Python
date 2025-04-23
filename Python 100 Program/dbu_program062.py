#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 62 :


# Write a program to read an ASCII string and
# to convert it to a unicode string encoded by utf-8.

# Hints:
# Use unicode() function to convert.

def main(sentence):
    ans = unicode(sentence, "utf-8")
    print ans

if __name__ == '__main__':
    try:
        sentence = raw_input('Enter any sentence: ')
        main(sentence)
    except ValueError:
        print 'Check Value'
