#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 70:

# Please write assert statements to verify that
# every number in the list [2,4,6,8] is even.

# Hints:
# Use "assert expression" to make assertion.


def main(values):

    for num in values:
        assert int(num) % 2 == 0

if __name__ == '__main__':
    try:
        values = [int(num) for num in raw_input("enter no:").split(",")]
        main(values)
    except (ValueError, AssertionError):
        print 'All values are not even in list or not in interger'
