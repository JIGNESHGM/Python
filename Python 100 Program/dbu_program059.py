#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 59 :

# Assuming that we have some email addresses
# in the "username@companyname.com" format,
# please write program to print the company name of a given email address.
# Both user names and company names are composed of letters only.

# Example:
# If the following email address is given as input to the program:

# john@google.com

# Then, the output of the program should be:

# google

# In case of input data being supplied to the question, it should be
# assumed to be a console input.

# Hints:
# Use \w to match letters.

import re


def main(EmailAddress):

    key = "(\w+)@(\w+).(\w+)"
    ans = re.match(key, EmailAddress)
    print ans.group(2)

if __name__ == '__main__':

    try:
        EmailAddress = raw_input('Enter an EmailAddress : ')
        main(EmailAddress)
    except ValueError:
        print 'Check Value'
