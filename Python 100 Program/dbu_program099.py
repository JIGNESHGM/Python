#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 99:

# Please write a program which prints all permutations of [1,2,3]

# Hints:
# Use itertools.permutations() to get permutations of list.

import itertools


def main(values):

    print list(itertools.permutations(values))

if __name__ == '__main__':
    try:
        values = [int(num) for num in raw_input("enter no:").split(",")]
        main(values)
    except ValueError:
        print 'Check Value'
