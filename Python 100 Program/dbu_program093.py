#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 93:

# With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155],
# write a program to make a list whose elements are intersection of the
# above given lists.

# Hints:
# Use set() and "&=" to do set intersection operation.


def main():

    set1 = set(raw_input('Enter Set1:  ').split(','))
    set2 = set(raw_input('Enter Set2:  ').split(','))

    set1 &= set2
    lis = list(set1)
    print lis


if __name__ == '__main__':
    main()
