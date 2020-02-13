from typing import List
from graph_commons import Vertice
import numpy as np


def demukron_network_order_function(vertices: List[Vertice], adj_matrix: np.ndarray) -> np.ndarray:
    """
    Demukron algorithm for network order function calculation for a given DAG in adjacency matrix representation.
    :param vertices: array of Vertice objects representing a set of vertices of the DAG
    :param adj_matrix: 2-dimensional adjacency matrix of ones and zeroes representing an existence of edges,
    the DAG in this case has no edge weights.
    :return: an array of network order degrees for the given vertices

    vertices are essentially unused, but provided just for the potential reference.
    """
    current_level = 0
    vertice_indices_set = set(range(len(vertices)))
    m = adj_matrix.sum(axis=0)  # array of in-degrees
    degrees_array = np.zeros(len(vertices))

    while vertice_indices_set:
        zero_on_the_current_step = {i for i in vertice_indices_set if m[i] == 0}
        for i in zero_on_the_current_step:
            degrees_array[i] = current_level
            m = m - adj_matrix[i]
        vertice_indices_set = vertice_indices_set - zero_on_the_current_step
        current_level += 1
    return degrees_array
