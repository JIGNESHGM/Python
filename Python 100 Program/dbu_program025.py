#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 25 :

# Define a class, which have a class parameter and have a same instance
# parameter.

# Hints:
# Define a instance parameter, need add it in __init__ method
# You can init a object with construct parameter or set the value later


def main():

    class person:

        def __init__(self, name):
            self.name = name

        def info(self):
            print 'Your name is {}'.format(self.name)

    name1 = person(raw_input('Enter your name: '))
    name1.info()

    name2 = person(raw_input('Enter your name: '))
    name2.info()


if __name__ == '__main__':
    main()
