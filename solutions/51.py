#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler
from common import all_digits_rev_lst
from common import get_resource_file
from itertools import combinations


###############################################################################
# Constants                                                                          #
###############################################################################

PRIME_FILENAME = "primes1-1000000.txt"


###############################################################################
# Problem                                                                     #
###############################################################################

class FamRoot(object):

    def __init__(self, fam_size):
        super(FamRoot, self).__init__()
        self.children = {}
        self.fam_size = fam_size

    def add(self, num):

        digits = all_digits_rev_lst(num)
        num_digits = len(digits)

        if num_digits not in self.children:
            self.children[num_digits] = FamTree(num_digits,
                                                self.fam_size)

        return self.children[num_digits].add(num, digits)


class FamTree(object):

    def __init__(self, num_digits, fam_size):
        super(FamTree, self).__init__()
        self.num_digits = num_digits
        self.positions = list(range(num_digits))
        self.pos_tuples = self.all_pos_tuples()
        self.children = {}
        self.fam_size = fam_size

    def all_pos_tuples(self):
        pos_tuples = []
        for length in range(1, self.num_digits):
            pos_tuples.extend(combinations(self.positions, length))
        return pos_tuples

    def all_vals(self, digits):
        for pos_tuple in self.pos_tuples:

            vals = set(digits[x] for x in pos_tuple)

            if len(vals) == 1:
                yield pos_tuple, vals

    def add(self, num, digits):

        results = []
        for pos_tuple, vals in self.all_vals(digits):

            if pos_tuple not in self.children:
                self.children[pos_tuple] = FamTemplate(pos_tuple,
                                                       self.fam_size)

            results.append(self.children[pos_tuple].add(num, digits))

        return min((x for x in results if x), default=None)


class FamTemplate(object):

    def __init__(self, pos_tuple, fam_size):
        super(FamTemplate, self).__init__()
        self.pos_tuple = pos_tuple
        self.children = {}
        self.fam_size = fam_size

    def add(self, num, digits):
        mask = []
        for pos, digit in enumerate(digits):
            if pos not in self.pos_tuple:
                mask.append(digit)
        mask = tuple(mask)

        if mask not in self.children:
            self.children[mask] = Fam(mask, self.fam_size)

        return self.children[mask].add(num)


class Fam(object):

    def __init__(self, mask, fam_size):
        super(Fam, self).__init__()
        self.mask = mask
        self.members = set()
        self.fam_size = fam_size

    def add(self, num):
        self.members.add(num)
        if len(self.members) >= self.fam_size:
            return min(self.members)
        else:
            return None


def read_primes(prime_filename):
    prime_filepath = get_resource_file(prime_filename)
    with open(prime_filepath) as prime_file:
        text = prime_file.read()

    primes = [int(x) for x in text.split()]

    return primes


class Problem51(Euler):

    def __init__(self):
        super().__init__("fam_size", 8)

    def solve(self):

        root = FamRoot(self.fam_size)

        for i in read_primes(PRIME_FILENAME):
            result = root.add(i)
            if result:
                return result


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem51().out()
