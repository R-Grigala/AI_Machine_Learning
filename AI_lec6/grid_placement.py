import random


# Generate an n x m grid and randomly place P objects labeled as 'P'
def generate_grid_with_objects(n, m, P):
    # Initialize the grid with '-' to represent empty spaces
    grid = []
    for i in range(n):
        raw = []
        for j in range(m):
            raw.append('-')
        grid.append(raw)

    # Ensure P does not exceed the grid capacity
    if P > n * m:
        raise ValueError("Number of objects exceeds the grid capacity")

    placed_objects = 0
    while placed_objects < P:
        # Randomly select a position
        row = random.randint(0, n - 1)
        col = random.randint(0, m - 1)

        # Place 'P' if the position is empty
        if grid[row][col] == '-':
            grid[row][col] = 'P'
            placed_objects += 1

    # Convert the grid to a string for pretty printing
    #    grid_str = ""
    #    for row in grid:
    #        grid_str += ' '.join(row) + "\n"

    grid_str = ""
    for row in grid:
        row_str = ""
        for element in row:
            row_str += element + " "
        grid_str += row_str + "\n"

    return grid, grid_str


# Draw the grid

print(generate_grid_with_objects(15, 15, 8)[1])
