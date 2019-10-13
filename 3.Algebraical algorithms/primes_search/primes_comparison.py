import timeit
import primes_search
import random

if __name__ == '__main__':
    print(timeit.timeit("primes_search.count_primes_brute_force(100000)",
                        globals=globals(), number=1))
    print(timeit.timeit("primes_search.count_primes_with_caching(100000)",
                        globals=globals(), number=1))
    print(timeit.timeit("primes_search.eratosthenes_sieve(100000)",
                        globals=globals(), number=1))
