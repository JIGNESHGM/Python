#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 15 :

# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# Hints:
# In case of input data being supplied to the question,
# it should be assumed to be a console input.


def main(num):

    ans1 = num
    ans2 = ans1 + (num * 10)
    ans3 = ans2 + (num * 100)
    ans4 = ans3 + (num * 1000)
    ans = ans1 + ans2 + ans3 + ans4
    return ans

if __name__ == '__main__':
    try:
        num = int(raw_input())
        print main(num)
    except ValueError:
        print 'Check Value'
