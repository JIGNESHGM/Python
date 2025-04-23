#!/user/bin/python
# -*- coding: utf-8 -*-

# program002 :

# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.

# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

# Hints:
# In case of input data being supplied to the question, it should be
# assumed to be a console input.


# all logic should be in side main method only


def main(fact):
    if fact == 0:
        return 1
    return fact * main(fact - 1)

if __name__ == '__main__':
    try:
        fact = int(raw_input('Enter number: '))
        print main(fact)
    except ValueError:
        print 'Check Value'
