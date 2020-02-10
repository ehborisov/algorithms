import unittest

from kosaraju import kosaraju_connected_components
from graph_commons import AdjacentListGraph
from parameterized import parameterized


class KosarajuTest(unittest.TestCase):

    @parameterized.expand(
        [
            [None, [1, 2, 3],
             [
                 [None, None, None],
                 [None, None, None],
                 [None, None, None]
             ],
             ([1, ], [2, ], [3, ])],

            [None, [1, 2, 3],
             [
                [None, 2, None],
                [1, None, None],
                [None, None, None]
             ],
             ([1, 2], [3, ])],

            [None, [1, 2, 3, 4, 5],
             [
                 [None, 2, None, None, None],
                 [1, None, None, None, None],
                 [None, None, None, 3, None],
                 [None, None, None, None, 2],
                 [None, None, None, 1, None]
             ], ([1, 2], [3, ], [4, 5])],

            [None, [1, 2, 3, 4, 5],
             [
                 [None, 2, None, None, None],
                 [1, None, None, None, None],
                 [None, None, None, 3, None],
                 [None, None, None, None, 2],
                 [None, None, None, 1, None]
             ], ([1, 2], [3, ], [4, 5])],

            [None, [1, 2, 3, 4, 5],
             [
                 [None, 2, None, None, None],
                 [None, None, 1, None, None],
                 [None, 2, None, 3, None],
                 [None, None, 2, None, 2],
                 [None, None, None, None, None]
             ], ([1, ], [2, 3, 4], [5, ])],

            [None, [1, 2, 3, 4, 5],
             [
                 [None, None, None, None, 1],
                 [None, None, 2, None, 1],
                 [None, None, None, 2, 1],
                 [None, 2, None, None, 1],
                 [None, None, None, None, None]
             ], ([1, ], [2, 3, 4], [5, ])],
        ]
    )
    def test_kosaraju_connected_components(self, _, vertices, matrix, expected_components):
        graph = AdjacentListGraph.construct_from_matrix(vertices, matrix)
        components = kosaraju_connected_components(graph)
        assert sorted([[v.key for v in cc.vertices] for cc in components]) == sorted(expected_components)


if __name__ == '__main__':
    unittest.main()
