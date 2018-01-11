#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse


###############################################################################
# Constants                                                                   #
###############################################################################

UPPER_LIMIT = 1000


###############################################################################
# Problem                                                                     #
###############################################################################

def threeFiveMultiplesSum_itr(upper_limit):

    total = 0

    for num in range(upper_limit):
        if isDivisible(num):
            total += num

    return total


def threeFiveMultiplesSum_func(upper_limit):

    nums = range(upper_limit)
    filtered = filter(isDivisible, nums)
    answer = sum(filtered)

    return answer


###############################################################################
# Helper functions                                                                          #
###############################################################################

def isDivisible(num):
    return num % 5 == 0 or num % 3 == 0


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit",
                        type=int,
                        default=UPPER_LIMIT)
    return parser.parse_args()


###############################################################################
# Main script                                                                 #
###############################################################################

def main():

    args = get_args()

    answer = threeFiveMultiplesSum_func(args.limit)

    print(answer)


if __name__ == '__main__':
    main()
