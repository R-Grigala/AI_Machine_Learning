class PriorityQueue:
    def __init__(self):
        self.queue = []

    # Inserts an item into the queue and maintains the sorted order based on cost
    def push(self, item):

        inserted = False
        for i in range(len(self.queue)):
            if item[0] < self.queue[i][0]:  # Compare costs
                self.queue.insert(i, item)
                inserted = True
                break
        if not inserted:
            self.queue.append(item)

    # Pops the item with the smallest cost from the queue.
    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    # Checks if the queue is empty.
    def is_empty(self):
        return len(self.queue) == 0


def uniform_cost_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.push((0, [start]))  # (cost, path)
    explored = set()

    while not frontier.is_empty():
        cost, path = frontier.pop()
        node = path[-1]
        print(f"Exploring node {node} with cost {cost}.")

        if node in explored:
            continue

        explored.add(node)

        if node == goal:
            return (cost, path)

        for neighbor, step_cost in graph[node]:
            if neighbor not in explored:
                new_cost = cost + step_cost
                new_path = path + [neighbor]
                frontier.push((new_cost, new_path))

    return None


# Example graph
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('C', 2), ('D', 7)],
    'C': [('A', 5), ('B', 2), ('D', 1)],
    'D': [('B', 7), ('C', 1)]
}

# run the search with custom priority queue
print(graph)
print('-------')
cost, path = uniform_cost_search(graph, 'A', 'D')
print(f"Path found: {path} with total cost {cost}")


