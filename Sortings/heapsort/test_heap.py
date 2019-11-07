import unittest
import heapq

from random import randint
from heapsort.heap import MaxHeap, MinHeap
from copy import copy
from parameterized import parameterized


class HeapBuildingTest(unittest.TestCase):

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
    def test_min_heap(self, _, n):
        expected = [randint(-1000, 1000) for _ in range(n)]

        data_copy = copy(expected)
        heapq.heapify(expected)
        assert MinHeap.build_min_heap(data_copy).storage == expected

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
    def test_max_heap(self, _, n):
        expected = [randint(-1000, 1000) for _ in range(n)]
        data_copy = copy(expected)
        heapq._heapify_max(expected)
        assert MaxHeap.build_max_heap(data_copy).storage == expected


if __name__ == '__main__':
    unittest.main()
