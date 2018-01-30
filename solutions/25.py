#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler
from common import fib_gen, all_digits


###############################################################################
# Problem                                                                     #
###############################################################################

def num_digits(num):
    return len(list(all_digits(num)))


def nth_digit_fib(n):
    for idx, f in enumerate(fib_gen(), start=2):
        if num_digits(f) >= n:
            return idx


class Problem25(Euler):

    def __init__(self):
        super().__init__("num_digits", 1000)

    def solve(self):
        return nth_digit_fib(self.num_digits)


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem25().out()
