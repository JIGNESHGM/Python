#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 23 :

# Write a method which can calculate square value of number

# Hints:
# Using the ** operator


def main(main):
    return num ** 2

if __name__ == '__main__':
    try:
        num = int(raw_input('Entre an integer number: '))
        print main(num)
    except ValueError:
        print 'Check Value'
