#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
from itertools import product as cartesian

###############################################################################
# Constants                                                                   #
###############################################################################

DIGITS = 3


###############################################################################
# Problem                                                                     #
###############################################################################

def largest_palindrome_naive(num_digits):
    max_val = 10 ** num_digits - 1

    palindromes = (x for x in products(max_val)
                   if is_palindrome(x))

    return max(palindromes)


def products(max_val):
    for a, b in cartesian(multiplicands(max_val),
                          repeat=2):
        yield a * b


def multiplicands(max_val):
    return range(max_val, 0, -1)


def digits(num):
    factor = 1
    while factor < num:
        yield int(num % (factor * 10) / factor)
        factor *= 10


def is_palindrome(num):
    digs = list(digits(num))
    return digs == list(reversed(digs))


###############################################################################
# Helper functions                                                            #
###############################################################################

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--digits",
                        type=int,
                        default=DIGITS)
    return parser.parse_args()


###############################################################################
# Main script                                                                 #
###############################################################################

def main():

    args = get_args()

    print(largest_palindrome_naive(args.digits))


if __name__ == '__main__':
    main()
