#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
from common import divisible, is_prime, next_factor
from itertools import combinations
from functools import reduce
from operator import mul


###############################################################################
# Constants                                                                   #
###############################################################################

NUM_DIVISORS = 500


###############################################################################
# Problem                                                                     #
###############################################################################

def triangle_number(num_divisors):
    return next(x for x in triangles()
                if num_factors(x) > num_divisors)


def triangles():
    increment = 0
    num = 0
    while True:
        increment += 1
        num += increment
        yield num


def num_factors(num):
    return len(factor(num))


def factor(num):

    primes = prime_factors(num)
    factors = set()

    for length in range(1, len(primes)):
        for comb in combinations(primes, length):
            new_factor = reduce(mul, comb)
            factors.add(new_factor)

    return factors


def next_prime_factor(num, cur):
    candidate = next_factor(num, cur)
    while not is_prime(candidate):
        candidate = next_factor(num, candidate)
    return candidate


def prime_factors(num):

    target = num
    current = 2
    factors = []

    while not is_prime(target):

        if not divisible(target, current):
            current = next_prime_factor(target, current)

        target //= current
        factors.append(current)

    return factors + [target]


###############################################################################
# Helper functions                                                            #
###############################################################################

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-divisors",
                        type=int,
                        default=NUM_DIVISORS)
    return parser.parse_args()


###############################################################################
# Main script                                                                 #
###############################################################################

def main():

    args = get_args()

    print(triangle_number(args.num_divisors))


if __name__ == '__main__':
    main()
