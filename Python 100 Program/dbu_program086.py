#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 86:

# Please write a program to generate all sentences where
# subject is in ["I", "You"] and verb is in ["Play", "Love"]
# and the object is in ["Hockey","Football"].

# Hints:
# Use list[index] notation to get a element from a list.


def main():

    str1 = [cnt for cnt in raw_input().split(',')]
    str2 = [cnt for cnt in raw_input().split(',')]
    str3 = [cnt for cnt in raw_input().split(',')]

    print

    for item1 in range(len(str1)):
        for item2 in range(len(str2)):
            for item3 in range(len(str3)):
                sentence = "%s %s %s." % (
                    str1[item1], str2[item2], str3[item3])
                print sentence

if __name__ == '__main__':
    main()
