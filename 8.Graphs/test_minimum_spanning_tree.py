import unittest

from kruskal import kruskal_minimum_spanning_tree
from prim import prim_minimum_spanning_tree, PrimVertice
from graph_commons import AdjacentListGraph
from parameterized import parameterized


def construct_graph_from_matrix(keys, weights) -> AdjacentListGraph:
    vertices_mapping = {key: PrimVertice(key) for key in keys}
    graph = AdjacentListGraph(vertices=vertices_mapping.values())
    for i in range(len(weights)):
        for j in range(len(weights)):
            if weights[i][j] is not None:
                graph.add_edge(vertices_mapping[keys[i]], vertices_mapping[keys[j]], weights[i][j])
    return graph


class MinimumSpanningTreeTest(unittest.TestCase):

    @parameterized.expand([
        [None, [1, 2, 3],
         [
             [None, 1, None],
             [None, None, 1],
             [None, None, None]
         ],
         ((1, 2, 1), (2, 3, 1))
         ],
        [None, [1, 2, 3],
         [
             [None, 1, 3],
             [None, None, 2],
             [None, None, None]
         ],
         ((1, 2, 1), (2, 3, 2))],

        [None, [1, 2, 3, 4, 5],
         [
             [None, 1, 3, 1, 4],
             [None, None, 2, None, None],
             [None, None, None, 2, None],
             [None, None, None, None, 1],
             [None, None, None, 2, None]
         ], ((1, 2, 1), (1, 4, 1), (2, 3, 2), (4, 5, 1))],

        [None, [1, 2, 3, 4, 5],
         [
             [None, 5, 2, None, 3],
             [None, None, 4, None, 3],
             [None, None, None, 1, None],
             [None, None, None, None, 1],
             [None, None, None, None, None]
         ], ((1, 3, 2), (2, 5, 3), (3, 4, 1), (4, 5, 1))],

        [None, [1, 2, 3, 4, 5],
         [
             [None, None, None, None, 2],
             [None, None, 3, None, None],
             [1, None, None, None, 1],
             [2, None, None, None, 2],
             [None, 4, None, 1, None]
         ], ((1, 3, 1), (1, 4, 2), (2, 3, 3), (3, 5, 1))],

        [None, [1, 2, 3, 4, 5],
         [
             [None, 4, None, 2, 2],
             [1, None, 2, None, 1],
             [3, None, None, None, 2],
             [None, None, 1, None, None],
             [1, None, None, None, 3]
         ], ((1, 4, 2), (1, 5, 2), (2, 5, 1), (3, 4, 1))]
    ])
    def test_kruskal_minimum_spanning_tree(self, _, vertices, matrix, expected_edges):
        graph = construct_graph_from_matrix(vertices, matrix)
        mst = kruskal_minimum_spanning_tree(graph)
        edges = [(v_from.key, v_to.key, w) for v_from, v_to, w in mst.edges]
        assert sorted(edges) == sorted(expected_edges)

    @parameterized.expand([
        [None, [1, 2, 3],
         [
             [None, 1, None],
             [None, None, 1],
             [None, None, None]
         ],
         ((1, 2, 1), (2, 3, 1))
         ],
        [None, [1, 2, 3],
         [
             [None, 1, 3],
             [None, None, 2],
             [None, None, None]
         ],
         ((1, 2, 1), (2, 3, 2))],

        [None, [1, 2, 3, 4, 5],
         [
             [None, 1, 3, 1, 4],
             [None, None, 2, None, None],
             [None, None, None, 2, None],
             [None, None, None, None, 1],
             [None, None, None, 2, None]
         ], ((1, 2, 1), (1, 3, 3), (1, 4, 1), (4, 5, 1))],

        [None, [1, 2, 3, 4, 5],
         [
             [None, 5, 2, None, 3],
             [None, None, 4, None, 3],
             [None, None, None, 1, None],
             [None, None, None, None, 1],
             [None, None, None, None, None]
         ], ((1, 3, 2), (1, 5, 3), (2, 5, 3), (3, 4, 1))],

        [None, [1, 2, 3, 4, 5],
         [
             [None, None, None, None, 2],
             [None, None, 3, None, None],
             [1, None, None, None, 1],
             [2, None, None, None, 2],
             [None, 4, None, 1, None]
         ], ((1, 3, 1), (1, 4, 2), (2, 3, 3), (3, 5, 1))],

        [None, [1, 2, 3, 4, 5],
         [
             [None, 4, None, 2, 2],
             [1, None, 2, None, 1],
             [3, None, None, None, 2],
             [None, None, 1, None, None],
             [1, None, None, None, 3]
         ], ((1, 3, 3), (1, 5, 2), (2, 5, 1), (3, 4, 1))]
    ])
    def test_prim_minimum_spanning_tree(self, _, vertices, matrix, expected_edges):
        graph = construct_graph_from_matrix(vertices, matrix)
        mst = prim_minimum_spanning_tree(graph, graph.vertices[0])
        edges = [(v_from.key, v_to.key, w) for v_from, v_to, w in mst.edges]
        assert sorted(edges) == sorted(expected_edges)

    @parameterized.expand([
        [None, [1, 2, 3, 4, 5, 6], 3,
         [
             [None, 1, 2, None, None, None, 1],
             [None, None, 2, 2, 3, None],
             [None, None, None, 2, None, 2],
             [None, None, None, None, None, 1],
             [None, None, None, None, None, 2],
             [None, None, None, None, None, None]
         ], ((1, 2, 1), (2, 4, 2), (3, 4, 2), (4, 6, 1), (5, 6, 2))],

        [None, [1, 2, 3, 4, 5, 6], 5,
         [
             [None, 1, 2, None, None, None, 1],
             [None, None, 2, 2, 3, None],
             [None, None, None, 2, None, 2],
             [None, None, None, None, None, 1],
             [None, None, None, None, None, 2],
             [None, None, None, None, None, None]
         ], ((1, 2, 1), (2, 3, 2), (3, 6, 2), (4, 6, 1), (5, 6, 2))]
        ]
    )
    def test_prim_minimum_spanning_tree_with_starting_point(self, _, vertices, starting_vertice_index, matrix,
                                                            expected_edges):
        graph = construct_graph_from_matrix(vertices, matrix)
        mst = prim_minimum_spanning_tree(graph, graph.vertices[starting_vertice_index])
        edges = [(v_from.key, v_to.key, w) for v_from, v_to, w in mst.edges]
        assert sorted(edges) == sorted(expected_edges)


if __name__ == '__main__':
    unittest.main()
