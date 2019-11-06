import unittest

from heapsort import heapsort
from random import shuffle
from copy import copy
from parameterized import parameterized


class HeapsortTest(unittest.TestCase):

    @parameterized.expand(
        [
            [None, 0],
            [None, 1],
            [None, 2],
            [None, 3],
            [None, 5],
            [None, 10],
            [None, 17],
            [None, 1000],
        ]
    )
    def test_exponentiation(self, _, n):
        expected = list(range(n)) if n else []
        shuffled = copy(expected)
        shuffle(shuffled)
        assert heapsort.heapsort(shuffled) == expected


if __name__ == '__main__':
    unittest.main()
