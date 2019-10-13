import math


def count_primes_brute_force(p: int) -> int:
    c = 1
    for i in range(2, p + 1):
        for j in range(2, i):
            if i % j == 0:
                c += 1
                break
    return p - c


def count_primes_with_caching(p: int) -> int:
    primes = [2]
    for i in range(3, p + 2, 2):
        is_prime = True
        sqrt_i = math.sqrt(i)
        for j in primes:
            if j > sqrt_i:
                break
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return len(primes)


def eratosthenes_sieve(p: int) -> int:
    table = [True for _ in range(p+1)]
    table[0] = False
    table[1] = False
    t = 2
    while t ** 2 < p:
        if table[t]:
            for i in range(t * 2, p + 1, t):
                table[i] = False
        t += 1
    c = 0
    for k in range(p+1):
        if table[k]:
            c += 1
    return c
