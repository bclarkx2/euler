#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler, get_resource_file


###############################################################################
# Problem                                                                     #
###############################################################################

def read_names(f):
    with open(f) as name_file:
        name_string = name_file.readline()

    names = name_string.split(",")
    names = [name.replace("\"", "") for name in names]

    return sorted(names)


def word_score(word):
    return sum(ord(letter) - 64 for letter in word)


def score(names):
    total = 0
    for pos, name in enumerate(names, start=1):
        total += pos * word_score(name)
    return total


class Problem22(Euler):

    def __init__(self):
        super().__init__("filename", 0)

    def solve(self):
        path = get_resource_file("p022_names.txt")
        names = read_names(path)
        return score(names)


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem22().out()
