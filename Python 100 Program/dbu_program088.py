#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 88:

# By using list comprehension, please write a program
# to print the list after removing delete numbers
# which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# Hints:
# Use list comprehension to delete a bunch of element from a list.


def main():

    return lis

if __name__ == '__main__':

    try:
        lis = [int(cnt) for cnt in raw_input().split(',')
               if int(cnt) % 5 != 0 and int(cnt) % 7 != 0]
        print main()
    except ValueError:
        print 'please Enter Integer numbers Only...'
