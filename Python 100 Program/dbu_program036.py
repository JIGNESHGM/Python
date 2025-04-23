#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 36 :

# Define a function which can generate a dictionary
# where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the
# keys only.

# Hints:
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to
# get key/value pairs.


def main(num1, num2):
    dic = dict()
    if num1 < num2:
        for cnt in range(num1, num2 + 1):
            dic[cnt] = cnt ** 2
        for value in dic.keys():
            print value
    else:
        print 'Ending range must be greater than starting range'

if __name__ == '__main__':
    try:
        num1 = int(raw_input('Enter starting range: '))
        num2 = int(raw_input('Enter ending range: '))
        main(num1, num2)
    except ValueError:
        print 'check value'
