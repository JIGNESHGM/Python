#!/usr/bin/python
# -*- coding: utf-8 -*-

# program 20 :

# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.

# Hints:
# Consider use yield


def main(num):

    class iterator:

        def show(self):

            cnt = 0
            while cnt <= num:
                if cnt % 7 == 0:
                    yield cnt
                cnt += 1

        result = []
        for cnt in show(num):
            result.append(str(cnt))

        print ",".join(result)

    fun = iterator()
    fun.show()

if __name__ == '__main__':
    try:
        num = int(raw_input("Enter an integer number : "))
        main(num)
    except ValueError:
        print 'Check Input'
