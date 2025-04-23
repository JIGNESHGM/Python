#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 68:

# Please write a program using generator to
# print the even numbers between 0 and n in
# comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:

# 10

# Then, the output of the program should be:

# 0,2,4,6,8,10

# Hints:
# Use yield to produce the next value in generator.

# In case of input data being supplied to the question,
# it should be assumed to be a console input.


def main(num):

    def fun(num):
        cnt = 0
        while cnt <= num:
            if cnt % 2 == 0:
                yield cnt
            cnt += 1

    values = []
    for cnt in fun(num):
        values.append(str(cnt))

    print ",".join(values)

if __name__ == '__main__':
    try:
        num = int(raw_input('Enter any number: '))
        main(num)
    except ValueError:
        print 'Check value'
