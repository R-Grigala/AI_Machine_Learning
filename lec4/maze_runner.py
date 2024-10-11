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


# Input maze
maze_str = """
########
#S  ## #
###    #
#  ##  #
## #  ##
#  ## F#
########

"""
maze_str1 = '''
###############
#S# ## #      #
# #    # #### #
# # # ## #  # #
# # #      #  #
#  #  ####  # #
# #  #    # # #
#  ## # #  #  #
# #   #  # ## #
# # # # #   # #
#   #   # #  F#
###############
'''

# Convert input maze to a list of lists
maze = []
maze_lines = maze_str.strip().splitlines()  # Split the input string into lines
for line in maze_lines:
    row = []
    for char in line:
        row.append(char)  # Add each character to the row list
    maze.append(row)  # Add the completed row to the maze list
#print(maze)

# Solve the maze and print the result
solve_maze(maze)
