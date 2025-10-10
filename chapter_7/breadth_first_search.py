from collections import deque


def BFS(graph, start):
    """
    Perform Breadth-First Search of the graph starting from Vertex u.
    """
    visited = {start: None}
    queue = deque([start])

    while queue:
        current = queue.popleft()

        for neighbor in graph.get_adjacent_vertices(current):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    return visited
