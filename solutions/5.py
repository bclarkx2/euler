#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
from operator import mul
from functools import reduce

###############################################################################
# Constants                                                                   #
###############################################################################

NUMBER = 20


###############################################################################
# Problem                                                                     #
###############################################################################

def smallest_divisible(num):
    facts = real_factors(num)
    candidate = reduce(mul, facts)

    divisor = 1
    while divisor:
        candidate //= divisor
        divisor = largest_divisor(candidate, facts)

    return candidate


def largest_divisor(candidate, factors):

    for factor in factors:
        new_candidate = candidate // factor
        if all_divisible(new_candidate, factors):
            return factor
    return None


def all_divisible(candidate, factors):
    return all(divisible(candidate, x)
               for x in factors)


def divisible(a, b):
    return a % b == 0


def real_factors(num):
    factors = range(2, num + 1)
    return list(reversed(factors))


###############################################################################
# Helper functions                                                            #
###############################################################################

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--number",
                        type=int,
                        default=NUMBER)
    return parser.parse_args()


###############################################################################
# Main script                                                                 #
###############################################################################

def main():

    args = get_args()

    print(smallest_divisible(args.number))


if __name__ == '__main__':
    main()
