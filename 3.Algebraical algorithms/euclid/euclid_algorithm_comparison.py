import timeit
import euclid_gcd
import random

if __name__ == '__main__':
    print(timeit.timeit("euclid_gcd.gcd_subtraction(random.randint(1, 1e10), random.randint(1, 1e10))",
                        globals=globals()))
    print(timeit.timeit("euclid_gcd.gcd_division(random.randint(1, 1e10), random.randint(1, 1e10))",
                        globals=globals()))
    print(timeit.timeit("euclid_gcd.gcd_bitwise(random.randint(1, 1e10), random.randint(1, 1e10))",
                        globals=globals()))
