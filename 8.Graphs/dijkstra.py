import bintrees
from typing import Tuple, List
from math import inf

from graph_commons import AdjacentListGraph, SPVertice


def dijkstra_shortest_paths(graph: AdjacentListGraph, start: SPVertice):
    visited = set()
    start.shortest_path_estimate = 0
    q = bintrees.RBTree()
    for v in graph.vertices:
        q.insert(v, v.shortest_path_estimate)
    while not q.is_empty():
        u, current_sp_eta = q.min_item()
        q.remove(u)
        visited.add(u)
        for adj_v, w in graph[u].items():
            if adj_v in visited:
                continue
            if adj_v.shortest_path_estimate > current_sp_eta + w:
                adj_v.previous = u
                q.remove(adj_v)
                adj_v.shortest_path_estimate = current_sp_eta + w
                q.insert(adj_v, adj_v.shortest_path_estimate)


def dijkstra_shortest_path(graph: AdjacentListGraph, start: SPVertice, end: SPVertice) -> Tuple[int, List[SPVertice]]:
    visited = set()
    start.shortest_path_estimate = 0
    q = bintrees.RBTree()
    for v in graph.vertices:
        q.insert(v, v.shortest_path_estimate)
    while not q.is_empty():
        u, current_sp_eta = q.min_item()
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
            if adj_v.shortest_path_estimate > current_sp_eta + w:
                adj_v.previous = u
                q.remove(adj_v)
                adj_v.shortest_path_estimate = current_sp_eta + w
                q.insert(adj_v, adj_v.shortest_path_estimate)
    return inf, []
