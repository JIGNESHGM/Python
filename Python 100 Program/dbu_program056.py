#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 56 :

# Write a function to compute 5/0 and use try/except to catch the exceptions.

# Hints:
# Use try/except to catch exceptions.


def main():
    return 5 / 0

if __name__ == '__main__':
    try:
        main()

    except ZeroDivisionError:
        print "Divide by zero ERROR!"

    except Exception, err:
        print 'Caught an exception'

    finally:
        print 'In finally block for cleanup'
