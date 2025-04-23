#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 95:

# Define a class Person and its two child classes: Male and Female. All
# classes have a method "getGender" which can print "Male" for Male class
# and "Female" for Female class.

# Hints:
# Use Subclass(Parentclass) to define a child class.


def main():

    class person(object):

        def getGender(self):
            return 'Unknown'

    class male(person):

        def getGender(self):
            return 'Male'

    class female(person):

        def getGender(self):
            return 'Female'

    isMale = male()
    isFemale = female()

    print isMale.getGender()
    print isFemale.getGender()

if __name__ == '__main__':
    main()
