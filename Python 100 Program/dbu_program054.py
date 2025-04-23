#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 54 :

# Define a class named Shape and its subclass Square.
# The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape
# where Shape's area is 0 by default.

# Hints:
# To override a method in super class,
# we can define a method with the same name in the super class.


def main():

    class Shape(object):

        def __init__(self, length):
            self.length = length

        def area(self):
            return 0

    class Square(Shape):

        def __init__(self, length):
            self.length = length

        def area(self):
            print self.length * self.length

    ans = Square(int(raw_input('Enter Length of Square: ')))
    ans.area()


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print 'Check Value'
