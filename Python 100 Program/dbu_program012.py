#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 12 :

# Write a program, which will find all such numbers
# between 1000 and 3000 (both included) such
# that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on
# a single line.

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


def main(start, end):

    values = []
    for cnt in range(start, end):
        dig = str(cnt)
        if((int(dig[0]) % 2 == 0) and
           (int(dig[1]) % 2 == 0) and
           (int(dig[2]) % 2 == 0) and
           (int(dig[3]) % 2 == 0)):
            values.append(dig)
    return ",".join(values)

if __name__ == '__main__':
    try:
        start = int(raw_input('Enter Number One:'))
        end = int(raw_input('Enter Number Two:'))
        print main(start, end)
    except ValueError:
        print 'Check Value'
