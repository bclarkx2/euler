#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler
import itertools


###############################################################################
# Constants                                                                   #
###############################################################################

VALUES = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]


###############################################################################
# Problem                                                                     #
###############################################################################

class Tree(object):

    def __init__(self, val, left, right):
        super().__init__()
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def make(cls, lis, idx):
        if idx >= len(lis):
            return None
        val = lis[idx]
        left = cls.make(lis, Tree.left_child(idx))
        right = cls.make(lis, Tree.right_child(idx))
        return Tree(val, left, right)

    @staticmethod
    def left_child(idx):
        total = 0
        for num in itertools.count(1):
            total += num
            if total > idx:
                return idx + num

    @staticmethod
    def right_child(idx):
        return Tree.left_child(idx) + 1

    def max_path(self):

        if self.left is None:
            return self.val
        else:
            return self.val + \
                max(self.left.max_path(),
                    self.right.max_path())

    def __repr__(self):
        return "\n".join(self.to_str(0))

    def to_str(self, indent):
        lines = []
        lines.append(" " * indent + str(self.val))
        if self.left:
            lines.extend(self.left.to_str(indent + 1))
        if self.right:
            lines.extend(self.right.to_str(indent + 1))
        return lines


class Problem18(Euler):

    def __init__(self):
        super().__init__("arg", 0)

    def solve(self):
        vals = [item for sublist in VALUES
                for item in sublist]
        tree = Tree.make(vals, 0)
        return tree.max_path()


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem18().out()
