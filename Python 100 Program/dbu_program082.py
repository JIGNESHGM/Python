#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 82:

# Please write a program to compress and decompress
# the string "hello world!hello world!hello world!hello world!".

# Hints:
# Use zlib.compress() and zlib.decompress()
# to compress and decompress a string.

import zlib


def main():

    string = raw_input('Enter String: ')

    ans = zlib.compress(string)
    print 'Compressed String:  ' + ans
    print 'decompressed String:  ' + zlib.decompress(ans)

if __name__ == '__main__':
    main()
