import unittest

from bellman_ford import bellman_ford_shortest_paths
from dijkstra import dijkstra_shortest_paths
from graph_commons import AdjacentListGraph, SPVertice
from parameterized import parameterized
from math import inf


def construct_graph_from_matrix(keys, weights) -> AdjacentListGraph:
    vertices_mapping = {key: SPVertice(key) for key in keys}
    graph = AdjacentListGraph(vertices=vertices_mapping.values(), directed=True)
    for i in range(len(weights)):
        for j in range(len(weights)):
            if weights[i][j] is not None:
                graph.add_edge(vertices_mapping[keys[i]], vertices_mapping[keys[j]], weights[i][j])
    return graph


class ShortestPathsTest(unittest.TestCase):

    @parameterized.expand([
        [None, [1, 2, 3], 0,
         [
             [None, 1, None],
             [None, None, 1],
             [None, None, None]
         ],
         ((1, None, 0), (2, 1, 1), (3, 2, 2))
         ],
        [None, [1, 2, 3], 1,
         [
             [None, 1, 3],
             [None, None, 2],
             [None, None, None]
         ],
         ((1, None, inf), (2, None, 0), (3, 2, 2))
         ],

        [None, [1, 2, 3], 1,
         [
             [None, 1, -1],
             [1, None, 2],
             [None, 1, None]
         ],
         ((1, 2, 1), (2, None, 0), (3, 1, 0))
         ],

        [None, [1, 2, 3, 4, 5], 2,
         [
             [None, 1, 3, 1, 4],
             [None, None, 2, None, None],
             [None, None, None, 2, None],
             [None, None, None, None, 1],
             [1, None, None, 2, None]
         ],
         ((3, None, 0), (4, 3, 2), (5, 4, 3), (1, 5, 4), (2, 1, 5))
         ],

        [None, [1, 2, 3, 4, 5], 0,
         [
             [None, 5, 2, None, 3],
             [None, None, 4, None, 3],
             [None, None, None, 1, None],
             [None, None, None, None, 1],
             [-1, None, -2, None, None]
         ], ((1, None, 0), (2, 1, 5), (3, 5, 1), (4, 3, 2), (5, 1, 3))
         ],

        [None, [1, 2, 3, 4, 5], 3,
         [
             [None, None, None, None, 2],
             [None, None, 3, None, None],
             [1, None, None, None, 1],
             [2, None, None, None, 2],
             [None, 4, None, 1, None]
         ],
         ((4, None, 0), (5, 4, 2), (1, 4, 2), (2, 5, 6), (3, 2, 9))
         ],

        [None, [1, 2, 3, 4, 5], 2,
         [
             [None, 4, None, 2, 2],
             [1, None, 2, None, 1],
             [3, None, None, None, 2],
             [None, None, 1, None, None],
             [1, None, 1, None, None]
         ], ((3, None, 0), (5, 3, 2), (1, 3, 3), (4, 1, 5), (2, 1, 7))
         ]
    ])
    def test_bellman_ford_shortest_path_positive(self, _, vertices, start_vertice_index, matrix, expected_vertices):
        graph = construct_graph_from_matrix(vertices, matrix)
        result = bellman_ford_shortest_paths(graph, graph.vertices[start_vertice_index])
        assert result
        assert sorted(expected_vertices) == sorted([(v.key, v.previous.key if v.previous else None,
                                                     v.shortest_path_estimate) for v in graph.vertices])

    @parameterized.expand([
            [None, [1, 2, 3], 0,
             [
                 [None, 1, None],
                 [None, None, 1],
                 [None, -2, None]
             ]],

            [None, [1, 2, 3, 4, 5], 0,
             [
                 [None, 5, 2, None, None],
                 [None, None, 4, None, 3],
                 [None, None, None, 1, None],
                 [None, None, None, None, 1],
                 [-5, None, -2, None, None]
             ]]
        ])
    def test_bellman_ford_shortest_path_negative_cycle(self, _, vertices, start_vertice_index, matrix):
        graph = construct_graph_from_matrix(vertices, matrix)
        result = bellman_ford_shortest_paths(graph, graph.vertices[start_vertice_index])
        assert not result

    @parameterized.expand([
        [None, [1, 2, 3], 0,
         [
             [None, 1, None],
             [None, None, 1],
             [None, None, None]
         ],
         ((1, None, 0), (2, 1, 1), (3, 2, 2))
         ],
        [None, [1, 2, 3], 1,
         [
             [None, 1, 3],
             [None, None, 2],
             [None, None, None]
         ],
         ((1, None, inf), (2, None, 0), (3, 2, 2))
         ],

        [None, [1, 2, 3, 4, 5], 2,
         [
             [None, 1, 3, 1, 4],
             [None, None, 2, None, None],
             [None, None, None, 2, None],
             [None, None, None, None, 1],
             [1, None, None, 2, None]
         ],
         ((3, None, 0), (4, 3, 2), (5, 4, 3), (1, 5, 4), (2, 1, 5))
         ],

        [None, [1, 2, 3, 4, 5], 3,
         [
             [None, None, None, None, 2],
             [None, None, 3, None, None],
             [1, None, None, None, 1],
             [2, None, None, None, 2],
             [None, 4, None, 1, None]
         ],
         ((4, None, 0), (5, 4, 2), (1, 4, 2), (2, 5, 6), (3, 2, 9))
         ],

        [None, [1, 2, 3, 4, 5], 2,
         [
             [None, 4, None, 2, 2],
             [1, None, 2, None, 1],
             [3, None, None, None, 2],
             [None, None, 1, None, None],
             [1, None, 1, None, None]
         ], ((3, None, 0), (5, 3, 2), (1, 3, 3), (4, 1, 5), (2, 1, 7))
        ]
    ])
    def test_dijkstra_shortest_path(self, _, vertices, start_vertice_index, matrix, expected_vertices):
        graph = construct_graph_from_matrix(vertices, matrix)
        dijkstra_shortest_paths(graph, graph.vertices[start_vertice_index])
        assert sorted(expected_vertices) == sorted([(v.key, v.previous.key if v.previous else None,
                                                     v.shortest_path_estimate) for v in graph.vertices])
