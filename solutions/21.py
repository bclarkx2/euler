#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler
from common import factor


###############################################################################
# Problem                                                                     #
###############################################################################

def factors(num):
    return factor(num).union({1})


def d(num):
    return sum(factors(num))


def d_sums(lim):
    res = {}
    for n in range(1, lim):
        if n not in res:
            res[n] = d(n)
    return res


def amicables(ds):
    res = []
    for n, d_sum in ds.items():
        if d_sum > n and d_sum < len(ds):
            if ds[d_sum] == n:
                res.extend([n, d_sum])
    return res


class Problem21(Euler):

    def __init__(self):
        super().__init__("lim", 10000)

    def solve(self):
        ds = d_sums(self.lim)
        amics = amicables(ds)
        print(ds)
        print(amics)
        return sum(amicables(ds))


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem21().out()
