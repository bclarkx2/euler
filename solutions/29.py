#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler
from itertools import product,tee


###############################################################################
# Problem                                                                     #
###############################################################################

def distinct_powers(n):

    powers = set()

    for a, b in each_pair(range(2, n+1)):
        powers.add(a ** b)

    return len(powers)


def each_pair(it):
    return product(*tee(it, 2))


class Problem29(Euler):

    def __init__(self):
        super().__init__("n",100)
        

    def solve(self):
        return distinct_powers(self.n)


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem29().out()
