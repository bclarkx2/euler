#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse


###############################################################################
# Constants                                                                   #
###############################################################################

NUMBER = 600851475143


###############################################################################
# Problem                                                                     #
###############################################################################

def is_prime(num):
    for factor in range(2, num):
        if divisible(num, factor):
            return False
    return True


def divisible(a, b):
    return a % b == 0


def next_factor(num, cur):
    factor = cur + 1
    while not divisible(num, factor):
        factor += 1
    return factor


def largest_prime_factor_div(product):

    target = product
    current = 1

    while not is_prime(target):
        current = next_factor(target, current)

        if is_prime(current):
            target //= current

    return target


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

    print(largest_prime_factor_div(args.number))


if __name__ == '__main__':
    main()
