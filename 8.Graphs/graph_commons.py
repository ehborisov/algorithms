from __future__ import annotations

from typing import Any, Iterable, List, Optional, Dict, Tuple
from enum import Enum
from math import inf
from functools import total_ordering


class Color(Enum):
    WHITE = 'w'
    GREY = 'g'
    BLACK = 'b'


class Vertice(object):

    def __init__(self, key: Any = None):
        self.key = key
        self.in_degree = 0
        self.out_degree = 0
        self.color = Color.WHITE
        self.d = None
        self.f = None
        self.previous = None

    def visit(self, step: Optional[int] = None) -> None:
        self.d = step
        self.color = Color.GREY

    def finalize(self, step: Optional[int] = None) -> None:
        self.f = step
        self.color = Color.BLACK

    @property
    def is_visited(self) -> bool:
        return self.color != Color.WHITE

    @property
    def is_finalized(self) -> bool:
        return self.color == Color.BLACK


@total_ordering
class SPVertice(Vertice):

    def __init__(self, key: Any = None):
        super().__init__(key)
        self.shortest_path_estimate = inf

    # this hack with additional ordering by key is needed to make it work with RBTree as TreeSet data structure
    def __lt__(self, other: SPVertice):
        if self.shortest_path_estimate != other.shortest_path_estimate:
            return self.shortest_path_estimate < other.shortest_path_estimate
        else:
            return self.key < other.key

    def __gt__(self, other: SPVertice):
        if self.shortest_path_estimate != other.shortest_path_estimate:
            return self.shortest_path_estimate > other.shortest_path_estimate
        else:
            return self.key > other.key

    def __eq__(self, other):
        return self is other or self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __str__(self):
        return f"SPVertice key: {self.key} shortest path estimate: {self.shortest_path_estimate}"


class ConnectedComponent(object):

    def __init__(self, vertices: Iterable[Vertice] = None):
        self.vertices = vertices or set()


class MatrixGraph(object):

    def __init__(self, vertices: List[Vertice] = None, directed=False):
        self._vertices = vertices or []
        self._graph = [[None] * len(vertices) for _ in range(len(vertices))] if vertices else []
        self._directed = directed

    def add_vertice(self, v: Vertice) -> None:
        self._vertices.append(v)
        for row in self._graph:
            row.append(None)
        self._graph.append([None] * len(self._vertices))

    def add_edge(self, x: Vertice, y: Vertice, weight=1) -> None:
        if x == y:
            return
        x_index = self._vertices.index(x)
        y_index = self._vertices.index(y)
        self._graph[x_index][y_index] = weight
        x.out_degree += 1
        y.in_degree += 1
        if not self._directed:
            self._graph[y_index][y_index] = weight

    def remove_edge(self, x: Vertice, y: Vertice) -> None:
        x_index = self._vertices.index(x)
        y_index = self._vertices.index(y)
        self._graph[x_index][y_index] = None
        x.out_degree -= 1
        y.in_degree -= 1
        if not self._directed:
            self._graph[y_index][x_index] = None

    def __iter__(self):
        return iter(self._graph)

    def __getitem__(self, i: int, j: int) -> Optional[Any]:
        return self._graph[i][j]

    def __str__(self):
        output_lines = ["  " + "  ".join(str(v.key) for v in self._vertices)]
        for v, v_list in zip(self._vertices, self._graph):
            adj_line = [str(v.key) if v else '.' for v in v_list]
            output_lines.append(f'{v.key} ' + "| ".join(adj_line))
        return '\n'.join(output_lines) + '\n\n'


class AdjacentListGraph(object):

    def __init__(self, vertices: Iterable[Vertice] = None, directed=False):
        self._graph = {v: {} for v in vertices} or {}
        self._directed = directed

    @classmethod
    def construct_from_dict(cls, data: Dict[Any, Dict[Any, int]]) -> AdjacentListGraph:
        vertices_mapping = {key: Vertice(key) for key in data}
        graph = AdjacentListGraph(vertices=vertices_mapping.values())
        for key, adj_links in data.items():
            for adj_key, weight in adj_links.items():
                graph.add_edge(vertices_mapping[key], vertices_mapping[adj_key], weight)
        return graph

    @classmethod
    def construct_from_matrix(cls, keys: List[Any], weights: List[List[Any]]) -> AdjacentListGraph:
        vertices_mapping = {key: Vertice(key) for key in keys}
        graph = AdjacentListGraph(vertices=vertices_mapping.values())
        for i in range(len(weights)):
            for j in range(len(weights)):
                if weights[i][j] is not None:
                    graph.add_edge(vertices_mapping[keys[i]], vertices_mapping[keys[j]], weights[i][j])
        return graph

    def copy(self):
        new_graph = AdjacentListGraph(vertices=self.vertices, directed=self._directed)
        new_graph._graph = self._graph.copy()
        return new_graph

    def add_vertice(self, v: Vertice) -> None:
        self._graph[v] = {}

    @property
    def size(self) -> int:
        return len(self._graph)

    @property
    def vertices(self) -> List[Vertice]:
        return list(self._graph.keys())

    @property
    def edges(self) -> Iterable[Tuple[Vertice, Vertice, float]]:
        if self._directed:
            return ((x, y, w) for x in self._graph for y, w in self._graph[x].items())
        else:
            # dirty hack to get the unique edges, I'm too lazy to invent something better then that here
            return ((x, y, w) for x in self._graph for y, w in self._graph[x].items() if x.key < y.key)

    def add_edge(self, x: Vertice, y: Vertice, weight: float=1) -> None:
        if x == y:
            return
        if y in self._graph[x]:
            return
        self._graph[x][y] = weight
        x.out_degree += 1
        y.in_degree += 1
        if not self._directed:
            self._graph[y][x] = weight

    def adjust_edge_weight(self, x: Vertice, y: Vertice, weight:float) -> None:
        if x == y:
            return
        if y in self._graph[x]:
            return
        self._graph[x][y] = weight
        if not self._directed:
            self._graph[y][x] = weight

    def remove_edge(self, x: Vertice, y: Vertice) -> None:
        if x not in self._graph:
            return
        if y not in self._graph[x]:
            raise Exception(f"There is no edge from {x} to {y}")
        self._graph[x].pop(y)
        x.out_degree -= 1
        y.in_degree -= 1
        if not self._directed:
            self._graph[y].pop(x)

    def transpose(self) -> AdjacentListGraph:
        if not self._directed:
            return self
        new_graph = AdjacentListGraph(self._graph, self._directed)
        for v in self._graph:
            v.in_degree = 0
            v.out_degree = 0
        for in_v, vertices in self._graph.values():
            for out_v, weight in vertices.values():
                new_graph[out_v][in_v] = weight
                out_v.out_degree += 1
                in_v.in_degree += 1
        return new_graph

    def __iter__(self):
        return iter(self._graph)

    def __getitem__(self, v: Vertice) -> Dict[Vertice, int]:
        return self._graph[v]

    def __str__(self):
        output_lines = ["  " + "  ".join(str(v.key) for v in self._graph)]
        for v, adj_list in self._graph.items():
            adj_line = [str(adj_list[v]) if v in adj_list else '.' for v in self._graph]
            output_lines.append(f'{v.key} ' + "| ".join(adj_line))
        return '\n'.join(output_lines) + '\n\n'


def dfs_with_coloring(graph: AdjacentListGraph) -> None:
    t = 0

    def dfs_visit(u: Vertice):
        nonlocal t
        t += 1
        u.visit(t)
        for adj_v in graph[u]:
            if not adj_v.is_visited:
                adj_v.previous = u
                dfs_visit(adj_v)
        t += 1
        u.finalize(t)

    for v in graph:
        if not v.is_visited:
            dfs_visit(v)


def dfs_with_cc_construction(graph: AdjacentListGraph) -> List[ConnectedComponent]:
    for v in graph:
        v.color = Color.WHITE
        v.previous = None

    connected_components = []

    def dfs_visit(u: Vertice, component: ConnectedComponent):
        u.visit()
        for adj_v in graph[u]:
            if not adj_v.is_visited:
                adj_v.previous = u
                component.vertices.add(adj_v)
                dfs_visit(adj_v, component)
        u.finalize()

    for v in graph:
        if not v.is_visited:
            cc = ConnectedComponent()
            cc.vertices.add(v)
            dfs_visit(v, cc)
            connected_components.append(cc)
    return connected_components
