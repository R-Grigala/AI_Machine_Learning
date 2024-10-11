from queue import PriorityQueue


def a_star_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    visited = set()
    parent = {start: None}  # Dictionary to keep track of the path
    path_cost = {start: 0}  # Dictionary to keep track of the cost of the path to each node

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

        visited.add(current)

        for neighbor in graph[current]:
            # Update the path cost for the neighbor, in this case, path cost is always 1
            new_cost = path_cost[current] + 1
            if neighbor not in path_cost or new_cost < path_cost[neighbor]:
                path_cost[neighbor] = new_cost
                total_cost = new_cost + heuristic[neighbor]
                frontier.put((total_cost, neighbor))
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
result = a_star_search(graph, 'A', 'H', heuristic)
if result:
    print("Path to goal found:", result)
else:
    print("No path found.")
