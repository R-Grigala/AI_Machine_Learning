from queue import PriorityQueue


def greedy_best_first_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    visited = set()
    parent = {start: None}  # Dictionary to keep track of the path

    while not frontier.empty():
        # Fetch the priority-node tuple and extract the node part
        priority_node_tuple = frontier.get()
        current = priority_node_tuple[1]

        if current == goal:
            # Reconstruct the path from start to goal
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Return reversed path

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    h_cost = heuristic[neighbor]
                    frontier.put((h_cost, neighbor))
                    # Update the parent of neighbor to be the current node
                    parent[neighbor] = current

    return None  # If the goal is not reachable


# Example graph represented as neighbors list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C', 'H'],
    'G': ['C'],
    'H': ['E', 'F']
}

# Example heuristic function values for each node to the goal (assuming goal is 'H')
heuristic = {
    'A': 3,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 1,
    'F': 3,
    'G': 3,
    'H': 0
}

# Execute the search
result = greedy_best_first_search(graph, 'A', 'H', heuristic)
if result:
    print("Path to goal found:", " -> ", result)   #.join(result))
else:
    print("No path found.")
