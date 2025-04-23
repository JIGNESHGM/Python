#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 80:

# Please write a program to randomly generate a
# list with5 numbers, which are divisible by 5 and 7 ,
# between 1 and 1000 inclusive.

# Hints:
# Use random.sample() to generate a list of random values.

import random


def main(num1, num2):
    if num1 < num2 and num2 >= 5:
        print random.sample([cnt for cnt in range(num1, num2 + 1)
                             if cnt % 5 == 0 and cnt % 7 == 0], 5)

    else:
        print 'Ending Range must be greater than 5 and starting range also ...'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter Starting Range: '))
        num2 = int(raw_input('Enter Ending Range: '))
        main(num1, num2)
    except ValueError:
        print 'Check Value'
