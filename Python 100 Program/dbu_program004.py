#!/user/bin/python
# -*- coding: utf-8 -*-

    # program004:

    # Write a program which accepts a sequence of comma-separated numbers
    # from console and generate a list and a tuple which contains every number.

    # Suppose the following input is supplied to the program:
    # 34,67,55,33,12,98

    # Then, the output should be:
    # ['34', '67', '55', '33', '12', '98']
    # ('34', '67', '55', '33', '12', '98')

    # Hints:
    # In case of input data being supplied to the question, it should be
    # assumed to be a console input.

    # tuple() method can convert list to tuple

    # all logic should be in side main method only


def main(num):

    lis = num.split(",")
    tup = tuple(lis)

    print lis
    print tup

if __name__ == '__main__':
    try:
        num = raw_input('Enter numbers (in Integer) : ')
        main(num)
    except ValueError:
        print 'Check Value'
