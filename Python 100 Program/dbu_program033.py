#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 33 :

# Define a function which can print a dictionary where the keys are numbers
# between 1 and 3 (both included) and the values are square of keys.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.


def main(num1, num2):

    dic = dict()
    if num1 < num2:
        for values in range(num1, num2 + 1):
            dic[values] = values ** values

        return dic

    else:
        print 'Ending range must be greater than starting range'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter Starting Range: '))
        num2 = int(raw_input('Enter Ending Range: '))
        print main(num1, num2)
    except ValueError:
        print 'Check Value'
