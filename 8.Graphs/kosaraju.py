from graph_commons import AdjacentListGraph, ConnectedComponent, dfs_with_coloring, dfs_with_cc_construction
from typing import Iterable


def kosaraju_connected_components(graph: AdjacentListGraph) -> Iterable[ConnectedComponent]:
    dfs_with_coloring(graph)
    t_graph = graph.transpose()
    return dfs_with_cc_construction(t_graph)
