#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 94:

# With a given list [12,24,35,24,88,120,155,88,120,155], write a program
# to print this list after removing all duplicate values with original
# order reserved.

# Hints:
# Use set() to store a number of values without duplicate.


def main():

    def removeDuplicate(list):
        newlist = []
        seen = set()
        for item in list:
            if item not in seen:
                seen.add(item)
                newlist.append(item)
        return newlist

    list = raw_input().split(',')
    print removeDuplicate(list)

if __name__ == '__main__':
    main()
