import unittest

from exponentiation import exponentiation_algorithms
import math
from parameterized import parameterized


class ExponentiationTest(unittest.TestCase):

    @parameterized.expand(
        [
            [None, 1, 0],
            [None, 1, 1],
            [None, 2, 2],
            [None, 2, 10],
            [None, 25, 10],
            [None, 10, 1],
            [None, 10, 10],
            [None, 123, 21],
            [None, 2, -1],
            [None, 10, -3],
        ]
    )
    def test_exponentiation(self, _, a, b):
        expected = a ** b
        self.assertTrue(math.isclose(expected, exponentiation_algorithms.naive_exponentiation(a, b)),
                        "Naive exponentiation algorithm error")
        self.assertTrue(math.isclose(expected, exponentiation_algorithms.squaring_exponentiation(a, b)),
                        "Squaring exponentiation algorithm error")
        self.assertTrue(math.isclose(expected, exponentiation_algorithms.power_of_two_with_multiplication(a, b)),
                        "Power of 2 with multiplication exponentiation algorithm error")


if __name__ == '__main__':
    unittest.main()
