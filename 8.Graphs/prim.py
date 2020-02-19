from __future__ import annotations

import heapq

from graph_commons import AdjacentListGraph, Vertice
from math import inf
from typing import Any
from functools import total_ordering


@total_ordering
class PrimVertice(Vertice):

    def __init__(self, key: Any = None):
        super().__init__(key)
        self.min_weight = inf

    def __lt__(self, other: PrimVertice):
        return self.min_weight < other.min_weight


def prim_minimum_spanning_tree(graph: AdjacentListGraph, start: PrimVertice) -> AdjacentListGraph:
    start.min_weight = 0
    q = graph.vertices
    heapq.heapify(q)

    while q:
        u = heapq.heappop(q)
        for adj_v, w in graph[u].items():
            if adj_v in q and w < adj_v.min_weight:
                adj_v.previous = u
                adj_v.min_weight = w

    mst = AdjacentListGraph(graph.vertices)
    for v in mst.vertices:
        if v.previous:
            mst.add_edge(v.previous, v, weight=v.min_weight)

    return mst
