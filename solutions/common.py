
###############################################################################
# Imports                                                                     #
###############################################################################

import argparse
import os
from itertools import combinations
from functools import reduce
from operator import mul


###############################################################################
# Classes                                                                     #
###############################################################################

class Euler(object):
    """base class to solve an Euler problem"""
    def __init__(self, arg_name, default_arg):
        super(Euler, self).__init__()
        self.arg_name = arg_name
        self.default_arg = default_arg

        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--" + arg_name,
                                 type=int,
                                 default=default_arg)
        self.args = self.parse_args()
        self.pull_main_arg()

    def add_argument(self, *args):
        return self.parser.add_argument(*args)

    def parse_args(self):
        return self.parser.parse_args()

    def pull_main_arg(self):
        setattr(self,
                self.arg_name,
                getattr(self.args, self.arg_name))

    def solve(self):
        raise NotImplementedError("provide solve method")

    def out(self):
        print(self.solve())


###############################################################################
# Utility                                                                     #
###############################################################################

def divisible(a, b):
    return a % b == 0


def is_prime(num):
    for factor in range(2, num):
        if divisible(num, factor):
            return False
    return True


def next_factor(num, cur):
    factor = cur + 1
    while not divisible(num, factor):
        factor += 1
    return factor


def digit(num, place):
    divisor = 10 ** place

    if divisor > num:
        return None

    latter = num % (divisor * 10)
    return latter // divisor


def all_digits(num):
    place = 0
    while 10 ** place < num:
        yield digit(num, place)
        place += 1


def next_prime_factor(num, cur):
    candidate = next_factor(num, cur)
    while not is_prime(candidate):
        candidate = next_factor(num, candidate)
    return candidate


def prime_factors(num):

    target = num
    current = 2
    factors = []

    while not is_prime(target):

        if not divisible(target, current):
            current = next_prime_factor(target, current)

        target //= current
        factors.append(current)

    return factors + [target]


def factor(num):

    primes = prime_factors(num)
    factors = set()

    for length in range(1, len(primes)):
        for comb in combinations(primes, length):
            new_factor = reduce(mul, comb)
            factors.add(new_factor)

    return factors


def get_resource_file(filename):
    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    parent_dir = os.path.dirname(current_dir)
    resource_dir = os.path.join(parent_dir, "resources")
    resource_path = os.path.join(resource_dir, filename)
    return resource_path


def factors(num):
    return factor(num).union({1})


def sum_of_factors(num):
    return sum(factors(num))


def all_factor_sums(lim):
    res = {}
    for n in range(1, lim):
        if n not in res:
            res[n] = sum_of_factors(n)
    return res
