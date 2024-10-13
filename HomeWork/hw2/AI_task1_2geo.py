import random

def create_empty_maze(n):
    """შექმნის ცარიელ ლაბირინთს, სადაც ყველა უჯრა დაბლოკილია ('#')."""
    return [['#' if i == 0 or j == 0 or i == n - 1 or j == n - 1 else '#' 
             for j in range(n)] for i in range(n)]

def generate_maze_with_path(n):
    """გენერირებს ლაბირინთს, სადაც იქნება მინიმუმ ერთი გზა S-დან F-მდე."""
    maze = create_empty_maze(n)

    # სტარტი და ფინიში
    maze[1][1] = 'S'
    maze[n - 2][n - 2] = 'F'

    def dfs(x, y):
        """DFS ალგორითმით შექმნის გზებს ლაბირინთში."""
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # მარჯვნივ, ქვემოთ, მარცხნივ, ზემოთ
        random.shuffle(directions)  # შემთხვევითი მიმართულებების არჩევა

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2  # ახალი უჯრა

            if 1 <= nx < n - 1 and 1 <= ny < n - 1 and maze[nx][ny] == '#':
                maze[x + dx][y + dy] = ' ' # ორი უჯრას შორის ხსნის გზას
                maze[nx][ny] = ' '  # ახალი უჯრა გახსნილი გზით
                dfs(nx, ny)

    # გზების გენერირება
    dfs(1, 1)

    # დარწმუნდით, რომ ფინიშთან მინიმუმ ერთი გზა არსებობს
    if maze[n - 2][n - 3] == '#' and maze[n - 3][n - 2] == '#':
        if random.choice([True, False]):
            maze[n - 2][n - 3] = ' '
        else:
            maze[n - 3][n - 2] = ' '

    return maze

def print_maze(maze):
    """ბეჭდავს ლაბირინთს ლამაზად."""
    for row in maze:
        print("".join(row))

def bfs(maze, start, end):
    """მოიძებნება გზა ლაბირინთში S-დან F-მდე BFS-ით."""
    rows, cols = len(maze), len(maze[0])
    queue = [start]
    visited = set([start])
    parent_map = {}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # ზემოთ, ქვემოთ, მარცხნივ, მარჯვნივ

    while queue:
        x, y = queue.pop(0)

        if (x, y) == end:
            # გზის აღდგენა
            while (x, y) != start:
                maze[x][y] = 'O'
                x, y = parent_map[(x, y)]
            maze[start[0]][start[1]] = 'S'
            maze[end[0]][end[1]] = 'F'
            return True

        # მეზობლის შემოწმება
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] in (' ', 'F') and (nx, ny) not in visited:
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent_map[(nx, ny)] = (x, y)

    return False  # ვერ მოიძებნა გზა

def solve_maze(maze):
    """მოიძებნება და დაბეჭდავს გზას, თუ ასეთი არსებობს."""
    start = end = None

    # მოძებნე სტარტი (S) და ფინიში (F)
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'F':
                end = (i, j)

    if not start or not end:
        print("სტარტი ან ფინიში ვერ მოიძებნა.")
        return

    if bfs(maze, start, end):
        print("მოიძებნა გზა:")
        print_maze(maze)
    else:
        print("გზა ვერ მოიძებნა.")

# ლაბირინთის ზომა
N = 15

# ლაბირინთის გენერირება და დაბეჭდვა
maze = generate_maze_with_path(N)
print("გენერირებული ლაბირინთი:")
print_maze(maze)

# ლაბირინთის ამოხსნა
# print("\nამოხსნილი ლაბირინთი:")
# solve_maze(maze)
