#! /usr/bin/env python3

###############################################################################
# Imports                                                                     #
###############################################################################

from common import Euler, divisible


###############################################################################
# Constants                                                                   #
###############################################################################

START = 1901


###############################################################################
# Problem                                                                     #
###############################################################################

def reg_year():
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def leap_year():
    regular = reg_year()
    regular[2] += 1
    return regular


def is_sunday(day):
    return divisible(day, 7)


def num_sundays(end):
    count = 1
    day = 2

    for year in range(START, end):
        months = leap_year() if divisible(year, 4) else reg_year()
        for month_days in months:
            count += is_sunday(day)
            day += month_days

    return count


class Problem19(Euler):

    def __init__(self):
        super().__init__("end", 2001)

    def solve(self):
        return num_sundays(self.end)


###############################################################################
# Main                                                                        #
###############################################################################

if __name__ == '__main__':
    Problem19().out()
