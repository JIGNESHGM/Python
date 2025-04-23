#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 96:

# Please write a program which count and print the numbers of each
# character in a string input by console.

# Example:
# If the following string is given as input to the program:

# abcdefgabc

# Then, the output of the program should be:

# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

# Hints:
# Use dict to store key/value pairs.
# Use dict.get() method to lookup a key with default value.


def main():

    dic = {}
    string = raw_input()
    for string in string:
        dic[string] = dic.get(string, 0) + 1
    print '\n'.join(['%s,%s' % (po1, po2) for po1, po2 in dic.items()])

if __name__ == '__main__':
    main()
