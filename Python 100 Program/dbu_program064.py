#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 64:

# Write a program to compute 1/2+2/3+3/4+...+n/n+1
# with a given n input by console (n>0).

# Example:
# If the following n is given as input to the program:

# 5

# Then, the output of the program should be:

# 3.55

# In case of input data being supplied to the question,
# it should be assumed to be a console input.

# Hints:
# Use float() to convert an integer to a float


def main(num):

    sum = 0.0

    if num > 0:
        for cnt in range(1, num + 1):
            sum += float(float(cnt) / (cnt + 1))
        print sum
    else:
        print 'Number should be greater then 0...'

if __name__ == '__main__':
    try:
        num = int(raw_input('Enter number: '))
        main(num)
    except ValueError:
        print 'Check Value'
