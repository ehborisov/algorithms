from graph_commons import AdjacentListGraph, SPVertice


def bellman_ford_shortest_paths(graph: AdjacentListGraph, start: SPVertice):
    start.shortest_path_estimate = 0

    edges = list(graph.edges)
    for i in range(graph.size - 1):
        for v_from, v_to, w in edges:
            if v_to.shortest_path_estimate > v_from.shortest_path_estimate + w:
                v_to.shortest_path_estimate = v_from.shortest_path_estimate + w
                v_to.previous = v_from

    for v_from, v_to, w in edges:
        if v_to.shortest_path_estimate > v_from.shortest_path_estimate + w:
            return False
    return True
