#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 53 :

# Define a class named Rectangle which can be
# constructed by a length and width.
# The Rectangle class has a method which can compute the area.

# Hints:
# Use def methodName(self) to define a method.


def main():

    class Rectangle(object):

        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            print self.length * self.width

    ans = Rectangle(int(raw_input('Enter Length: ')),
                    int(raw_input('Enter Width: ')))
    ans.area()

if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print 'Check Value'
