#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
from collections import OrderedDict


###############################################################################
# Constants                                                                   #
###############################################################################

MAX = 2000000


###############################################################################
# Problem                                                                     #
###############################################################################

def sum_of_primes(cap):

    nums = OrderedDict()
    primes = []

    for num in range(2, cap):
        nums[num] = None

    while nums:

        current, _ = nums.popitem(last=False)
        primes.append(current)

        multiple = 2 * current
        while multiple < cap:
            nums.pop(multiple, None)
            multiple += current

    return sum(primes)


###############################################################################
# Helper functions                                                            #
###############################################################################

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max",
                        type=int,
                        default=MAX)
    return parser.parse_args()


###############################################################################
# Main script                                                                 #
###############################################################################

def main():

    args = get_args()

    print(sum_of_primes(args.max))


if __name__ == '__main__':
    main()
