#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 92:

# By using list comprehension, please write a program to print the list
# after removing the value 24 in [12,24,35,24,88,120,155].

# Hints:
# Use list's remove method to delete a value.


def main():

    lis = raw_input().split(',')
    lis = [int(cnt) for cnt in lis if int(cnt) != 24]
    print lis

if __name__ == '__main__':
    main()
