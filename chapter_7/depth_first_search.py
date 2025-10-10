def DFS(graph, u, visited=None):
    """
    Perform Depth-First Search of the undiscovered portion of the graph starting at Vertex u.
    """
    if visited is None:
        visited = {u: None}

    for v in graph.get_adjacent_vertices(u):
        if v not in visited:
            visited[v] = u
            DFS(graph, v, visited)

    return visited
