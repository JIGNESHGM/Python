#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 84:

# Please write a program to shuffle
# and print the list [3,6,7,8].

# Hints:
# Use shuffle() function to shuffle a list.

from random import shuffle


def main(values):

    shuffle(values)
    return values

if __name__ == '__main__':
    try:
        values = [int(num) for num in raw_input("enter no:").split(",")]
        print main(values)
    except ValueError:
        print 'Check Value'
