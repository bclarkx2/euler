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

def diag_sum_recursive(n):

    # too small to sum!
    if n <= 1:
        return max(n, 0)

    # compute the value in the upper right corner
    largest = n**2

    # sum the corners going counter clockwise from upper right
    corner_sum = sum(largest - i * (n - 1) for i in range(4))

    # diagonals sum = sum of this layer's corners plus the sum of the inner square's diagonals
    return corner_sum + diag_sum_recursive(n - 2)


def diag_sum(n):
    """Find the sum of the diagonals of a square of size n """

    if n % 2 == 0:
        return ""
    else:
        return diag_sum_recursive(n)


class Problem28(Euler):

    def __init__(self):
        super().__init__("n", 1001)

    def solve(self):
        return diag_sum(self.n)


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem28().out()
