#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 51 :

# Define a class named American and its subclass NewYorker.

# Hints:
# Use class Subclass(ParentClass) to define a subclass.


def main():

    class American(object):
        print 'ParentClass called...'

    class NewYorker(American):
        print 'SubClass called...'

    American()
    NewYorker()

if __name__ == '__main__':
    main()
