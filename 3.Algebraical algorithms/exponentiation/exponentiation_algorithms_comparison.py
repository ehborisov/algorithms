import timeit
import exponentiation_algorithms
import random

if __name__ == '__main__':
    print(timeit.timeit("exponentiation_algorithms.naive_exponentiation(random.randint(1, 1e6),"
                        "random.randint(1, 1e2))",
                        globals=globals()))
    print(timeit.timeit("exponentiation_algorithms.power_of_two_with_multiplication(random.randint(1, 1e6),"
                        "random.randint(1, 1e2))",
                        globals=globals()))
    print(timeit.timeit("exponentiation_algorithms.squaring_exponentiation(random.randint(1, 1e6),"
                        "random.randint(1, 1e2))",
                        globals=globals()))
    print(timeit.timeit("random.randint(1, 1e6) ** random.randint(1, 1e2)", globals=globals()))
