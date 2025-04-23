#!/usr/bin/python
# -*- coding: utf-8 -*-

# program001 :

# Define the program name
# Write a program which will find all such numbers which are
# divisible by 7 but are not a multiple of 5, between 2000
# and 3200 (both included).

# The numbers obtained should be printed in a comma-separated
# sequence on a single line.

# Hints:
# Consider use range(#begin, #end) method

# all logic should be in side main method only


import logging


def main(start, end):
    arr1 = []
    for cnt in range(start, end):
        if (cnt % 7 == 0) and (cnt % 5 != 0):
            arr1.append(str(cnt))
    return ','.join(arr1)
if __name__ == '__main__':
    try:
        start = int(raw_Pinput('Enter Number One:'))
        end = int(raw_input('Enter Number Two:'))
        print 'Output is :' + main(start, end)
    except:
        logging.warning('Check Value')
