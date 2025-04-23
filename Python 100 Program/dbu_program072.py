#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 72:

# Please write a binary search function which
# searches an item in a sorted list.
# The function should return
# the index of element to be searched in the list.

# Hints:
# Use if/elif to deal with conditions.


def main(list, value):
    bottom = 0
    top = len(list) - 1
    index = -1
    while top >= bottom and index == -1:
        mid = int((top + bottom) / 2.0)
        if list[mid] == value:
            index = mid
        elif list[mid] > value:
            top = mid - 1
        else:
            bottom = mid + 1
    if index == -1:
        print 'Element does not exist in the list'
    else:
        return index

if __name__ == '__main__':
    try:
        list = [int(num) for num in raw_input().split(",")]
        value = int(raw_input('Enter Value of element: '))
        print main(list, value)
    except ValueError:
        print 'Check Value'
