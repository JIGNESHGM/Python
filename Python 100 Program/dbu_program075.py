#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 75:

# Please generate a random float where the
# value is between 5 and 95 using Python math module.

# Hints:
# Use random.random() to generate a random float in [0,1].

import random


def main(num1, num2):
    if num1 < num2:
        print random.uniform(num1, num2 + 1)
    else:
        print 'Ending range must be greater than starting range'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter starting range: '))
        num2 = int(raw_input('Enter ending range: '))
        main(num1, num2)
    except ValueError:
        print 'check value'
