#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse


###############################################################################
# Constants                                                                   #
###############################################################################

INITIAL_SEQ = [1, 2]
LIMIT = 4000000


###############################################################################
# Problem                                                                     #
###############################################################################

def fib_gen(limit):
    seq = INITIAL_SEQ
    while seq[-1] < limit:
        yield seq[-1]
        seq.append(seq[-1] + seq[-2])


def sum_of_even_fibonacci(limit):
    even_terms = filter(is_even, fib_gen(limit))
    even_sum = sum(even_terms)
    return even_sum


def is_even(num):
    return num % 2 == 0


###############################################################################
# Helper functions                                                            #
###############################################################################

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit",
                        type=int,
                        default=LIMIT)
    return parser.parse_args()


###############################################################################
# Main script                                                                 #
###############################################################################

def main():

    args = get_args()

    print(sum_of_even_fibonacci(args.limit))


if __name__ == '__main__':
    main()
