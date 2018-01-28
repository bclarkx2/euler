
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
