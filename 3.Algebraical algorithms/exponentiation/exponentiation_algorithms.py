from typing import Union


def naive_exponentiation(a: int, b: int) -> Union[int, float]:
    r = 1
    if b < 0:
        a = 1 / a
        b *= -1
    for i in range(b):
        r *= a
    return r


def power_of_two_with_multiplication(a: int, b: int) -> Union[int, float]:
    r = a
    pwr = 1
    previous = 0
    if b < 0:
        a = 1 / a
        r = a
        if b == -1:
            return a
        b *= -1
    while pwr * 2 <= b:
        r *= r
        pwr *= 2
        previous = pwr
    if pwr != b:
        for _ in range(b-previous):
            r *= a
    return r


def squaring_exponentiation(a: int, b: int) -> Union[int, float]:
    # https://en.wikipedia.org/wiki/Exponentiation_by_squaring
    r = 1
    if b < 0:
        a = 1 / a
        b *= -1
    if not b:
        return r
    while b > 0:
        if b % 2:
            r *= a
        a *= a
        b //= 2
    return r
