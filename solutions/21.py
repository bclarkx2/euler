#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler
from common import all_factor_sums


###############################################################################
# Problem                                                                     #
###############################################################################

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
        ds = all_factor_sums(self.lim)
        amics = amicables(ds)
        return sum(amics)


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem21().out()
