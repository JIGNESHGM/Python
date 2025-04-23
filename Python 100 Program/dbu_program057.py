#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 57 :


# Define a custom exception class which takes a string message as attribute.

# Hints:
# To define a custom exception, we need to define a class inherited from
# Exception.

def main():

    class MyError(Exception):

        def __init__(self, msg):
            self.msg = msg
    try:
        MyError()

    except ZeroDivisionError:
        print "Divide by zero ERROR!"

    except Exception:
        print 'Caught an Exception'

    finally:
        print 'In finally block for cleanup'

if __name__ == '__main__':
    main()
