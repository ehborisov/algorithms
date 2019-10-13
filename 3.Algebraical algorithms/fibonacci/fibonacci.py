import math
import numpy


def fibonacci_recursive(n):
    if n < 2:
        return 1
    else:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)


def fibonacci_iterative(n):
    if n < 2:
        return 1
    f1 = 1
    f2 = 1
    t = 0
    for _ in range(3, n+1):
        t = f1 + f2
        f1 = f2
        f2 = t
    return t


def fibonacci_golden_ratio(n):
    ratio = numpy.float128((1 + numpy.sqrt(5))/2)
    return int(numpy.floor(numpy.divide(numpy.float_power(ratio, n), numpy.sqrt(5)) - 0.5))


def fibonacci_matrix(n):
    # see https://medium.com/@andrew.chamberlain/the-linear-algebra-view-of-the-fibonacci-sequence-4e81f78935a3
    S = numpy.array([[(1 + math.sqrt(5)) / 2, (1 - math.sqrt(5)) / 2],
                     [1, 1]])
    l = numpy.array([[(1 + math.sqrt(5)) / 2, 0],
                     [0, (1 - math.sqrt(5)) / 2]])
    s = numpy.array([[(5 + math.sqrt(5))/10, ],
                     [(5 - math.sqrt(5))/10, ]])

    l_k = numpy.linalg.matrix_power(l, n - 2)
    res = numpy.matmul(numpy.matmul(S, l_k), s)
    return math.ceil(res[0][0])
