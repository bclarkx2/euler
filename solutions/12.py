#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
from common import factor


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
