#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
from operator import add
from functools import reduce


###############################################################################
# Constants                                                                   #
###############################################################################

NUMBER = 100


###############################################################################
# Problem                                                                     #
###############################################################################

def diff(num):

    sum_of_sqaures = reduce(add, squares(num))
    square_of_sum = sum(seq(num)) ** 2

    return square_of_sum - sum_of_sqaures


def seq(num):
    return range(1, num + 1)


def squares(num):
    return (x**2 for x in seq(num))


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

    print(diff(args.number))


if __name__ == '__main__':
    main()
