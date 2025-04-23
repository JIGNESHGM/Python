#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 52 :

# Define a class named Circle which can be constructed by a radius.
# The Circle class has a method which can compute the area.

# Hints:
# Use def methodName(self) to define a method.

import math


def main():

    class Circle(object):

        def __init__(self, rad):
            self.rad = rad

        def area(self):
            print math.pi * self.rad ** 2

    ans = Circle(int(raw_input('Enter Radius: ')))
    ans.area()

if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print 'Check Value'
