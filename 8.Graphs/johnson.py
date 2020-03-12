from typing import Optional
import numpy as np

from dijkstra import dijkstra_shortest_paths
from bellman_ford import bellman_ford_shortest_paths
from graph_commons import AdjacentListGraph, SPVertice


def johnsons_all_pairs_shortest_paths(graph: AdjacentListGraph) -> Optional[np.ndarray]:
    dummy_vertice = SPVertice(key=None)

    augmented_graph = graph.copy()
    augmented_graph.add_vertice(dummy_vertice)
    for v in graph.vertices:
        augmented_graph.add_edge(dummy_vertice, v, 0)

    has_negative_cycle = not bellman_ford_shortest_paths(augmented_graph, dummy_vertice)

    if has_negative_cycle:
        return

    # this original estimates are needed to be kept in order to adjust back the estimates after the dijkstra runs
    # (as the estimates on the vertice objects will be changing)
    augmented_estimates = {v.key: v.shortest_path_estimate for v in augmented_graph.vertices}

    # adjust weights on the original graph to run dijkstra on
    for x, y, w in augmented_graph.edges:
        if x != dummy_vertice and y != dummy_vertice:
            graph.adjust_edge_weight(x, y, w + x.shortest_path_estimate - y.shortest_path_estimate)

    shortest_path_matrix = np.zeros((graph.size, graph.size))
    vertices = graph.vertices
    for i in range(graph.size):
        dijkstra_shortest_paths(graph, vertices[i])
        for j in range(graph.size):
            shortest_path_matrix[i][j] = (vertices[j].shortest_path_estimate
                                          + augmented_estimates[vertices[j].key] - augmented_estimates[vertices[i].key])
    return shortest_path_matrix
