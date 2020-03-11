import unittest

from a_star import PlaneVertice, a_star
from graph_commons import AdjacentListGraph
from parameterized import parameterized


def construct_graph_from_matrix(vertices, weights) -> AdjacentListGraph:
    vertices_mapping = {key: PlaneVertice(x, y, key) for key, x, y in vertices}
    graph = AdjacentListGraph(vertices=vertices_mapping.values(), directed=True)
    for i in range(len(weights)):
        for j in range(len(weights)):
            if weights[i][j] is not None:
                graph.add_edge(vertices_mapping[vertices[i][0]], vertices_mapping[vertices[j][0]], weights[i][j])
    return graph


class AStarShortestPathsTest(unittest.TestCase):

    @parameterized.expand([
        [None, [(1, -4, -2), (2, -1, 2), (3, 1, -3)], 0, 2,
         [
             [None, 1, 4],
             [None, None, 3],
             [None, 2, None],
        ],
         4, [1, 3]],
    ])
    def test_a_star_shortest_path(self, _, vertices, start_vertice_index, end_vertice_index, matrix,
                                  expected_path_cost, expected_path):
        graph = construct_graph_from_matrix(vertices, matrix)
        path_cost, shortest_path = a_star(graph, graph.vertices[start_vertice_index], graph.vertices[end_vertice_index])
        print(path_cost, [v.key for v in shortest_path])
        assert path_cost == expected_path_cost
        assert [v.key for v in shortest_path] == expected_path
