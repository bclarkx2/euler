#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler
from itertools import permutations


###############################################################################
# Constants                                                                   #
###############################################################################

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


###############################################################################
# Problem                                                                     #
###############################################################################

def nth_permutation(n):
    perms = sorted(permutations(DIGITS))
    return "".join(perms[n])


class Problem24(Euler):

    def __init__(self):
        super().__init__("place", 999999)

    def solve(self):
        return nth_permutation(self.place)


###########################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem24().out()
