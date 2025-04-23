#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 83:

# Please write a program to print the running
# time of execution of "1+1" for 100 times.

# Hints:
# Use timeit() function to measure the running time.

from timeit import Timer


def main():

    time = Timer("for cnt in range(100):1+1")
    print time.timeit()

if __name__ == '__main__':
    main()
