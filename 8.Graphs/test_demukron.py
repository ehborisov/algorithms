import unittest
import numpy as np

from demukron import demukron_network_order_function
from parameterized import parameterized


class DemukronTest(unittest.TestCase):

    @parameterized.expand(
        [
            [None, [1, 2, 3],
             [
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]
             ],
             [0, 0, 0]],

            [None, [1, 2, 3],
             [
                 [0, 1, 0],
                 [0, 0, 1],
                 [0, 0, 0]
             ],
             ([0, 1, 2])],

            [None, [1, 2, 3, 4, 5],
             [
                 [0, 1, 0, 0, 0],
                 [0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0]
             ], [0, 1, 2, 0, 3]],

            [None, [1, 2, 3, 4, 5, 6],
             [
                 [0, 1, 0, 0, 0, 1],
                 [0, 0, 1, 0, 0, 1],
                 [0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0]
             ], ([0, 1, 2, 3, 4, 5])],

            [None, [1, 2, 3, 4, 5, 6],
             [
                 [0, 1, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 1],
                 [0, 0, 0, 0, 0, 0]
             ], [0, 1, 2, 0, 1, 2]]
        ]
    )
    def test_demukron_network_order_function(self, _, vertices, matrix, expected_ranks):
        graph = np.array(matrix)
        ranks = demukron_network_order_function(vertices, graph)
        assert expected_ranks == list(ranks)


if __name__ == '__main__':
    unittest.main()
