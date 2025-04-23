#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 87:

# Please write a program to print the list after
# removing delete even numbers in [5,6,77,45,22,12,24].

# Hints:
# Use list comprehension to delete a bunch of element from a list.


def main():

    return lis

if __name__ == '__main__':
    try:
        lis = [int(cnt) for cnt in raw_input().split(',') if int(cnt) % 2 != 0]
        print main()
    except ValueError:
        print 'Please Enter Integer Numbers Only...'
