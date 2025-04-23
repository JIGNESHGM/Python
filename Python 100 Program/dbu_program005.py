#!/user/bin/python
# -*- coding: utf-8 -*-

# program005:

# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters


def main():

    class iostring(object):

        def __init__(self):
            self.s = ""

        def getString(self):
            self.s = str(raw_input('Enter String : '))

        def printString(self):
            return self.s.upper()

        def test(self):
            return 'Test Function.... Tested.... OK'

    strObj = iostring()
    strObj.getString()
    print strObj.printString()
    print strObj.test()

if __name__ == '__main__':
    main()
