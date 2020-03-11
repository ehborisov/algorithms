import bintrees

from typing import List, Tuple, Any, Callable
from graph_commons import AdjacentListGraph, SPVertice
from math import sqrt, inf


class PlaneVertice(SPVertice):

    def __init__(self, x: float, y: float, key: Any = None):
        super().__init__(key)
        self.x = x
        self.y = y

    def __str__(self):
        return f"PlaneVertice key: {self.key} coordinates: ({self.x}; {self.y})" \
            f" shortest path estimate: {self.shortest_path_estimate}"


def h_euclid_dist(node: PlaneVertice, dest: PlaneVertice, const_multiplier: float = 1) -> float:
    dx = abs(node.x - dest.x)
    dy = abs(node.y - dest.y)
    return const_multiplier * sqrt(dx ** 2 + dy ** 2)


def a_star(graph: AdjacentListGraph, start: PlaneVertice, end: PlaneVertice, h_function: Callable = h_euclid_dist
           ) -> Tuple[int, List[PlaneVertice]]:
    visited = set()
    start.shortest_path_estimate = 0
    q = bintrees.RBTree()
    for v in graph.vertices:
        q.insert(v, v.shortest_path_estimate)
    while not q.is_empty():
        u, _ = q.min_item()
        q.remove(u)
        visited.add(u)
        if u == end:
            shortest_path = [u]
            while u.previous:
                u = u.previous
                shortest_path.append(u)
            return end.shortest_path_estimate, list(reversed(shortest_path))
        for adj_v, w in graph[u].items():
            if adj_v in visited:
                continue
            if adj_v.shortest_path_estimate > u.shortest_path_estimate + w:
                adj_v.previous = u
                q.remove(adj_v)
                adj_v.shortest_path_estimate = u.shortest_path_estimate + w
                q.insert(adj_v, adj_v.shortest_path_estimate + h_function(adj_v, end))
    return inf, []
