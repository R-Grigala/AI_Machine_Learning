import heapq
import itertools

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous
        self.empty_pos = self.find_empty()
        self.priority = self.moves + self.manhattan_distance()

    def find_empty(self):
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                if val == 0:  # 0 აღნიშნავს ცარიელ უჯრას
                    return (i, j)

    def manhattan_distance(self):
        """ევრისტიკული ფუნქცია: ყველა ფილისთვის Manhattan მანძილის ჯამი."""
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:  # ცარიელ უჯრას არ ვითვლით
                    target_x, target_y = divmod(value - 1, 3)
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance

    def neighbors(self):
        """აბრუნებს ცარიელი უჯრის შესაძლო მეზობელ მდგომარეობებს."""
        x, y = self.empty_pos
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # მარჯვნივ, ქვევით, მარცხნივ, ზემოთ
        neighbors = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                # გაცვლა ცარიელი უჯრასთან
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors

    def __lt__(self, other):
        return self.priority < other.priority

    def is_goal(self):
        """ამოწმებს, თუ მიღწეულია მიზნის მდგომარეობა."""
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.board == goal

    def display(self):
        """ბეჭდავს დაფას."""
        for row in self.board:
            print(row)
        print()

def solve_puzzle(start_board):
    """A* ალგორითმის გამოყენებით ამოხსნის 8-puzzle-ს."""
    start = PuzzleState(start_board)
    priority_queue = []
    heapq.heappush(priority_queue, start)
    visited = set()

    while priority_queue:
        current = heapq.heappop(priority_queue)

        if current.is_goal():
            return current

        visited.add(tuple(itertools.chain(*current.board)))

        for neighbor in current.neighbors():
            if tuple(itertools.chain(*neighbor.board)) not in visited:
                heapq.heappush(priority_queue, neighbor)

    return None

def print_solution(solution):
    """ბეჭდავს ამოხსნის ნაბიჯებს."""
    path = []
    state = solution
    while state:
        path.append(state)
        state = state.previous

    for step in reversed(path):
        step.display()

# საწყისი და მიზნის მდგომარეობები
start_board = [
    [1, 2, 3],
    [4, 0, 5],
    [7, 8, 6]
]

print("საწყისი კონფიგურაცია:")
for row in start_board:
    print(row)

solution = solve_puzzle(start_board)

if solution:
    print("\nამოხსნის ნაბიჯები:")
    print_solution(solution)
else:
    print("ამ ამოცანას არ აქვს ამოხსნა.")
