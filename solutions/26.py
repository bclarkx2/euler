#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler
from common import prime_factors, divisible
from functools import reduce
from operator import mul

###############################################################################
# Problem                                                                     #
###############################################################################


def naive_approach(maximum):
 
    return max(range(2, maximum), key=len_cycle)


def len_cycle(num):

    remaining = non_decimal_component(num)

    if remaining == 1:
        return 0
    
    length = 1
    candidate = 9
    while not divisible(candidate, remaining):
        length += 1
        candidate = (10 ** length) - 1
    
    return length


def non_decimal_component(num):
    factors = prime_factors(num)
    non_decimal_factors = filter(lambda x: x not in [2, 5], factors)
    non_decimal_component = reduce(mul, non_decimal_factors, 1)
    return non_decimal_component


class Problem26(Euler):

    def __init__(self):
        super().__init__("max", 1000)

    def solve(self):
        return naive_approach(self.max)


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem26().out()
