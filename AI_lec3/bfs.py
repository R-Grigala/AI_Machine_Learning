# breadth-first search
def bfs(graph, start):
    visited = set()  # Keep track of visited nodes
    queue = [start]  # Queue for BFS, initialized with the start node
    visited_order = []  # Order of visited nodes

    while queue:
        # Pop the first element from queue and print it
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            visited_order.append(vertex)

            # Queue all adjacent nodes of dequeued vertex and mark them as visited
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)
    # A list of nodes in the order they were visited
    return visited_order


# A dictionary representing an adjacency list of the graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G', 'F'],
    'F': ['C', 'E'],
    'G': ['E']
}

bfs_result = bfs(graph, 'A')
print(bfs_result)
