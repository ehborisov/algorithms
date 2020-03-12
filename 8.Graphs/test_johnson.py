import unittest
import numpy as np

from johnson import johnsons_all_pairs_shortest_paths
from graph_commons import AdjacentListGraph, SPVertice
from parameterized import parameterized


def construct_graph_from_matrix(keys, weights) -> AdjacentListGraph:
    vertices_mapping = {key: SPVertice(key) for key in keys}
    graph = AdjacentListGraph(vertices=vertices_mapping.values(), directed=True)
    for i in range(len(weights)):
        for j in range(len(weights)):
            if weights[i][j] is not None:
                graph.add_edge(vertices_mapping[keys[i]], vertices_mapping[keys[j]], weights[i][j])
    return graph


class AllShortestPathsTest(unittest.TestCase):

    @parameterized.expand([
        [None, [1, 2, 3],
         [
             [None, 1, None],
             [2, None, 1],
             [3, None, None]
         ],
         [
             [0, 1, 2],
             [2, 0, 1],
             [3, 4, 0]
         ],
         ],

        [None, [1, 2, 3, 4, 5],
         [
             [None, None, 3, None, None],
             [2, None, 1, None, 2],
             [3, None, None, None, 1],
             [3, 4, None, None, 7],
             [1, 2, None, 2, None]
         ],
         [
             [0, 6, 3, 6, 4],
             [2, 0, 1, 4, 2],
             [2, 3, 0, 3, 1],
             [3, 4, 5, 0, 6],
             [1, 2, 3, 2, 0]
         ],
         ],
    ])
    def test_johnsons_all_shortest_paths(self, _, vertices, matrix, expected_matrix):
        graph = construct_graph_from_matrix(vertices, matrix)
        shortest_paths_matrix = johnsons_all_pairs_shortest_paths(graph)
        assert np.array_equal(shortest_paths_matrix, np.array(expected_matrix, dtype=float))
