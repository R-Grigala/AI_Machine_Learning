# depth-first search
def dfs(graph, start):
    visited = set()  # Keep track of visited nodes
    stack = [start]  # Stack for DFS, start node as first element
    visited_order = []  # Order of visited nodes

    while stack:
        # Pop the last element from stack
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            visited_order.append(vertex)
            # print(vertex, visited_order)

            # Add all adjacent nodes of the popped vertex to the stack
            # reverse the order of neighbors before adding them, to have same node order as BFS
            for neighbour in reversed(graph[vertex]):
                if neighbour not in visited:
                    stack.append(neighbour)
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

dfs_result = dfs(graph, 'A')
print(dfs_result)
