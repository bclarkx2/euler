#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
import time


###############################################################################
# Constants                                                                   #
###############################################################################

NUMBER = 10001


###############################################################################
# Problem                                                                     #
###############################################################################

def prime(required_primes):
    num_primes = 0
    current = 1
    factors = set()
    while num_primes < required_primes:
        current += 1
        if is_prime(current, factors):
            num_primes += 1

        prune_factors(factors, current)

    return current


def prune_factors(factors, new):
    if not any(new % x == 0 for x in factors):
        factors.add(new)


def is_prime(num, factors):
    return all(num % x != 0 for x in factors)


###############################################################################
# Helper functions                                                            #
###############################################################################
#
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--primes",
                        type=int,
                        default=NUMBER)
    parser.add_argument("--time", "-t",
                        action="store_true")
    return parser.parse_args()


###############################################################################
# Main script                                                                 #
###############################################################################

def main():

    args = get_args()

    start_time = time.time()

    print(prime(args.primes))

    stop_time = time.time()

    if args.time:
        print("time elapsed: {}".format(stop_time - start_time))


if __name__ == '__main__':
    main()
