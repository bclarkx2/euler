#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler
from common import all_factor_sums
from itertools import combinations_with_replacement as choose


###############################################################################
# Problem                                                                     #
###############################################################################

def abundants(lim):
    factor_sums = all_factor_sums(lim)
    return [n for n, s in factor_sums.items() if s > n]


def abundant_sums(lim):
    return {sum(c) for c in
            choose(abundants(lim), 2)
            if sum(c) <= lim}


def sum_of_non_abundant(lim):

    nums = set(range(1, lim + 1))
    sums = abundant_sums(lim)

    non_abundant = nums - sums

    return sum(non_abundant)


class Problem23(Euler):

    def __init__(self):
        super().__init__("lim", 28123)

    def solve(self):
        return sum_of_non_abundant(self.lim)


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem23().out()
