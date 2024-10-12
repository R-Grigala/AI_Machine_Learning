import random

def create_empty_maze(n):
    """შექმნის ცარიელ ლაბირინთს, სადაც ყველა უჯრა გზა (' ')."""
    return [['#' if i == 0 or j == 0 or i == n - 1 or j == n - 1 else ' ' 
             for j in range(n)] for i in range(n)]

def generate_maze_with_path(n):
    """გენერირებს ლაბირინთს, სადაც იქნება მინიმუმ ერთი გზა S-დან F-მდე."""
    maze = create_empty_maze(n)

    # სტარტი და ფინიში
    maze[1][1] = 'S'
    maze[n - 2][n - 2] = 'F'
    def dfs(x, y):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # მარჯვნივ, ქვემოთ, მარცხნივ, ზემოთ
        # random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2  # ორჯერ ვიხტებით (ერთი უჯრა კედელი იქნება)
            print(nx, ny)
            if 1 <= nx < n - 1 and 1 <= ny < n - 1 and maze[nx][ny] == ' ':
                # გზა გავხსნათ და DFS გავაგრძელოთ
                maze[x + dx][y + dy] = ' '  # კედლის გატეხვა
                maze[nx][ny] = ' '  # ახალი უჯრა
                dfs(nx, ny)

    dfs(1,1)
    return maze

def print_maze(maze):
    for row in maze:
        for cell in row:
            print(cell, end='')  # Print each cell in the row without a newline
        print()  # Print a newline at the end of each row


def bfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    queue = [start]  # Using a list as the queue
    visited = set([start])
    parent_map = {}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    while queue:
        x, y = queue.pop(0)  # Pop the first element to mimic queue behavior

        if (x, y) == end:
            # Path found, reconstruct path
            while (x, y) != start:
                maze[x][y] = 'O'
                x, y = parent_map[(x, y)]
            maze[start[0]][start[1]] = 'S'
            maze[end[0]][end[1]] = 'F'
            return True

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] in (' ', 'F') and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent_map[(nx, ny)] = (x, y)
        # print(parent_map)
    return False  # No path found


def solve_maze(maze):
    start = end = None

    # Find start (S) and finish (F) positions
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'F':
                end = (i, j)

    if not start or not end:
        print("Start or finish not found in the maze.")
        return

    if bfs(maze, start, end):
        print("Path found:")
        print_maze(maze)
    else:
        print("No path found.")


# ლაბირინთის ზომა
N = 5

# ლაბირინთის გენერირება და დაბეჭდვა
maze = generate_maze_with_path(N)
print("Generated Maze:")
solve_maze(maze)
