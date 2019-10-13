import timeit
import fibonacci
import random

if __name__ == '__main__':
    # print(timeit.timeit("fibonacci.fibonacci_recursive(1000)",
    #                     globals=globals(), number=1))  # everybody knows it is damn slow
    print(timeit.timeit("fibonacci.fibonacci_iterative(1000)",
                        globals=globals()))
    print(timeit.timeit("fibonacci.fibonacci_golden_ratio(1000)",
                        globals=globals()))
    print(timeit.timeit("fibonacci.fibonacci_matrix(1000)",
                        globals=globals()))