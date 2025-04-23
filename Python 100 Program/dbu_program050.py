#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 50 :
# Define a class named American which has
# a static method called printNationality.

# Hints:
# Use @staticmethod decorator to define class static method.


def main():

    class American(object):

        @staticmethod
        def printNationality():
            print "America"

    anAmerican = American()
    anAmerican.printNationality()

if __name__ == '__main__':
    main()
