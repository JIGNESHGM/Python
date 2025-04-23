#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 81:

# Please write a program to randomly print
# an integer number between 7 and 15 inclusive.

# Hints:
# Use random.randrange() to a random integer in a given range.

import random


def main(num1, num2):
    if num1 < num2:
        print random.randrange(num1, num2 + 1)

    else:
        print 'Ending Range must be greater than starting range ...'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter Starting Range: '))
        num2 = int(raw_input('Enter Ending Range: '))
        main(num1, num2)
    except ValueError:
        print 'Check Value'
