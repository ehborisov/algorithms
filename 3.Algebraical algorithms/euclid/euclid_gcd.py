
def gcd_subtraction(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def gcd_division(a: int, b: int) -> int:
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def gcd_bitwise(a: int, b: int) -> int:
    # recursive algorithm from https://en.wikipedia.org/wiki/Binary_GCD_algorithm
    if a == b:
        return a
    if a == 0:
        return b
    if b == 0:
        return a

    a_is_even = ~a & 1
    b_is_even = ~b & 1
    if a_is_even and b_is_even:  # 2. gcd(u, v) = 2·gcd(u/2, v/2)
        return gcd_bitwise(a >> 1, b >> 1) << 1
    elif a_is_even or b_is_even:  # 3. gcd(u, v) = gcd(u/2, v) or gcd(u, v) = gcd(u, v/2)
        return gcd_bitwise(a >> 1, b) if a_is_even else gcd_bitwise(a, b >> 1)
    else:
        if a >= b:
            return gcd_bitwise((a - b) >> 1, b)  # 4.  gcd(u, v) = gcd((u − v)/2, v)
        else:
            return gcd_bitwise((b - a) >> 1, a)  # 4. gcd(u, v) = gcd((v − u)/2, u)
