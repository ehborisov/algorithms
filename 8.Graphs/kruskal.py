from graph_commons import AdjacentListGraph
from disjoint_set import DisjointSet


def kruskal_minimum_spanning_tree(graph: AdjacentListGraph) -> AdjacentListGraph:
    disjoint_set = DisjointSet(graph.vertices)
    mst_graph = AdjacentListGraph(graph.vertices)
    for v_from, v_to, w in sorted(graph.edges, key=lambda x: x[2]):
        if not disjoint_set.is_connected(v_from, v_to):
            mst_graph.add_edge(v_from, v_to, w)
            disjoint_set.connect(v_from, v_to)
    return mst_graph
