from __future__ import annotations

from graph_commons import Vertice, AdjacentListGraph
from typing import List


class DisjointSet(object):

    def __init__(self, vertices: List[Vertice]):
        self._vertices_mapping = {v: i for i, v in enumerate(vertices)}
        self._components = list(self._vertices_mapping.values())
        self._ranks = [1] * len(vertices)

    @classmethod
    def from_graph(cls, graph: AdjacentListGraph) -> DisjointSet:
        ds = DisjointSet(graph.vertices)
        for v_from in graph:
            for v_to in graph[v_from]:
                ds.connect(v_from, v_to)
        return ds

    def _find(self, component_index: int) -> int:
        while component_index != self._components[component_index]:
            self._components[component_index] = self._components[self._components[component_index]]
            component_index = self._components[component_index]
        return component_index

    def connect(self, x: Vertice, y: Vertice) -> None:
        x_index = self._vertices_mapping[x]
        y_index = self._vertices_mapping[y]
        x_component = self._find(x_index)
        y_component = self._find(y_index)
        if x_component == y_component:
            return
        if self._ranks[y_component] > self._ranks[x_component]:
            x_component, y_component = y_component, x_component
        self._components[y_component] = x_component
        self._ranks[x_component] += self._ranks[y_component]

    def is_connected(self, x: Vertice, y: Vertice) -> bool:
        return (self._find(self._components[self._vertices_mapping[x]])
                == self._find(self._components[self._vertices_mapping[y]]))
