#!/usr/bin/env python
# -*- coding: utf-8 -*-

# program 100:

# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?

# Hint:
# Use for loop to iterate all possible solutions.


def main(heads, legs):

    ans1 = heads * 2
    ans2 = legs - ans1
    rabbits = ans2 / 2
    chickens = heads - rabbits

    if (rabbits * 4 + chickens * 2) == legs:
        print
        print 'Rabits are {}'.format(rabbits)
        print 'chickens are {}'.format(chickens)
    else:
        print 'Check numbers of total_heads and total_legs...'

if __name__ == '__main__':
    try:
        heads = int(raw_input('Enter total_heads: '))
        legs = int(raw_input('Enter total_legs: '))
        main(heads, legs)
    except ValueError:
        print'Check Input'
