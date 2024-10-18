import random


# Calculate the Manhattan distance between two points.
def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


# Generate an n x m grid and randomly place P objects labeled as 'P'
def generate_grid_with_objects(n, m, P):
    # Initialize the grid with '-' to represent empty spaces
    grid = []
    for i in range(n):
        raw = []
        for j in range(m):
            raw.append('-')
        grid.append(raw)

    # grid = [['-' for _ in range(m)] for _ in range(n)]

    # Ensure P does not exceed the grid capacity
    if P > n * m:
        raise ValueError("Number of objects exceeds the grid capacity")

    # Randomly place 'P' objects
    placed_objects = 0
    while placed_objects < P:
        row = random.randint(0, n - 1)
        col = random.randint(0, m - 1)
        if grid[row][col] == '-':
            grid[row][col] = 'P'
            placed_objects += 1

    return grid


# Place 'W's on the grid using a hill climbing algorithm to minimize the total Manhattan distance to all 'P's.
def place_W(grid, num_w):
    n, m = len(grid), len(grid[0])
    ws_positions = []

    # Initial placement of 'W's
    # available_positions = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == '-']
    available_positions = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '-':
                available_positions.append((i, j))

    random.shuffle(available_positions)

    for i in range(num_w):
        x, y = available_positions.pop()
        grid[x][y] = 'W'
        ws_positions.append((x, y))

    # Hill climbing optimization
    for iteration in range(1000):  # Prevents infinite loops
        improved = False
        for i, (x, y) in enumerate(ws_positions):
            best_score = float('inf')
            best_pos = (x, y)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '-':
                    grid[x][y] = '-'
                    grid[nx][ny] = 'W'

                    score = 0
                    for px in range(n):
                        for py in range(m):
                            if grid[px][py] == 'P':
                                score += manhattan_distance(nx, ny, px, py)

                    if score < best_score:
                        best_score = score
                        best_pos = (nx, ny)
                    grid[nx][ny] = '-'
                    grid[x][y] = 'W'
            if best_pos != (x, y):
                grid[x][y] = '-'
                grid[best_pos[0]][best_pos[1]] = 'W'
                ws_positions[i] = best_pos
                improved = True
        if not improved:
            break

    # Convert the grid to a string for pretty printing
    result = ""
    for row in grid:
        row_str = ""
        for element in row:
            row_str += element + " "
        result += row_str + "\n"

    return result


# Example usage
grid = generate_grid_with_objects(10, 10, 5)
print(place_W(grid, 1))
