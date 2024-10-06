import random
import time


class Environment:
    def __init__(self, size=3):
        self.size = size
        self.grid = []
        for i in range(size):  # creating 3x3 grid with random values 0 or 1
            row = []
            for j in range(size):
                row.append(random.choice([0, 1]))
            self.grid.append(row)
        self.cleaned_cells = 0

    def is_dirty(self, x, y): # assuming 1 is dirty, check if room needs to be cleaned
        return self.grid[y][x] == 1

    def clean(self, x, y):
        if self.grid[y][x] == 1:
            self.grid[y][x] = 0
            self.cleaned_cells += 1

    def is_all_clean(self):
        for row in self.grid:  # see if all the rooms are clean
            if 1 in row:
                return False
        return True

    def display(self):
        for row in self.grid:  # print the rooms, for user to see
            for cell in row:
                if cell == 1:
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        print()


class Roomba:
    def __init__(self, env1):
        self.x = 0
        self.y = 0
        self.env = env1  # each roomba has its own house to clean

    def move_left(self):
        self.x = max(0, self.x - 1)

    def move_right(self):
        self.x = min(self.env.size - 1, self.x + 1)

    def move_up(self):
        self.y = max(0, self.y - 1)

    def move_down(self):
        self.y = min(self.env.size - 1, self.y + 1)

    def act(self):   # if room is dirty roomba cleans it, if already clean go to next room
        if self.env.is_dirty(self.x, self.y):
            self.env.clean(self.x, self.y)
            return 'cleaned'
        else:
            # Moving row by row, left to right and wrapping to the next row when at the edge
            if self.x < self.env.size - 1:
                self.move_right()  # Move to the next cell in the row
            else:
                if self.y < self.env.size - 1:  # If we haven't reached the last row, move down
                    self.move_down()  # Move down to the next row
                    self.x = 0  # Start from the leftmost position in the new row
            return "moved"


e1 = Environment(4)  # By default, size will be 3
r1 = Roomba(e1)
steps = 0

while not e1.is_all_clean() and steps < 40:
    print(f'Step: {steps}')
    e1.display()
    print(f'Agent is at ({r1.x}, {r1.y})')
    action = r1.act()
    print(f'Agent {action}\n')
    time.sleep(3)
    steps += 1

print('Final state:')
e1.display()
if e1.is_all_clean():
    print(f"Environment is clean! cleaned {e1.cleaned_cells} cells")
else:
    print("Reached maximum steps without cleaning the entire environment.")