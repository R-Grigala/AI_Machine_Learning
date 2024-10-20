import math

# Game State Class to represent the number of pebbles and whose turn it is
class PebbleGame:
    def __init__(self, pebbles):
        self.pebbles = pebbles

    # Function to determine if the current player loses (only one pebble left)
    def is_game_over(self):
        return self.pebbles == 1

    # Apply a move (1 or 2 pebbles taken)
    def make_move(self, pebbles_taken):
        if pebbles_taken != 1 and pebbles_taken != 2:
            print("Invalid move! You can only take 1 or 2 pebbles.")
            return  # Invalid move, don't change the game state
        self.pebbles -= pebbles_taken

    # Get the list of all valid moves from the current game state
    def get_valid_moves(self):
        if self.pebbles == 1:
            return []  # No valid moves, game is over
        elif self.pebbles == 2:
            return [1]  # Can take only one pebble
        else:
            return [1, 2]  # More than 2 pebbles, so both moves are valid

# Minimax algorithm
def minimax(pebble_game, is_maximizing_player):
    if pebble_game.is_game_over():
        if is_maximizing_player:
            return -1  # Maximizing player (AI) loses
        else:
            return 1  # Minimizing player (human) loses

    # Safety check: if no valid moves are available (shouldn't normally happen)
    valid_moves = pebble_game.get_valid_moves()
    if not valid_moves:
        return 0  # Treat as a draw

    if is_maximizing_player:
        max_eval = -math.inf
        for move in valid_moves:
            new_game_state = PebbleGame(pebble_game.pebbles - move)
            eval = minimax(new_game_state, False)  # Now it's the minimizing player's turn
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in valid_moves:
            new_game_state = PebbleGame(pebble_game.pebbles - move)
            eval = minimax(new_game_state, True)  # Now it's the maximizing player's turn
            min_eval = min(min_eval, eval)
        return min_eval

# Function for the AI to choose the best move
def find_best_move(pebble_game):
    best_move = None
    best_value = -math.inf  # Start with the worst possible score for the AI

    # Try all possible moves and choose the one with the best evaluation
    for move in pebble_game.get_valid_moves():
        new_game_state = PebbleGame(pebble_game.pebbles - move)
        move_value = minimax(new_game_state, False)  # Opponent's turn after AI moves
        if move_value > best_value:
            best_value = move_value
            best_move = move

    return best_move

# Example of simulating the game with AI as Player 1
def simulate_game(pebbles):
    game = PebbleGame(pebbles)
    turn = 1  # 1 for AI, -1 for human
    print(f"Starting game with {pebbles} pebbles.")

    while not game.is_game_over():
        if turn == 1:
            # AI's turn
            move = find_best_move(game)
            game.make_move(move)
            print(f"AI takes {move} pebbles. {game.pebbles} pebbles left.")
        else:
            # Simulate a human move (or accept user input)
            move = int(input("Take pebble(s) from the heap (1 or 2): "))
            if move not in [1, 2]:
                print("Invalid input! Please take either 1 or 2 pebbles.")
                continue  # Skip invalid input, ask again
            game.make_move(move)
            print(f"Human takes {move} pebbles. {game.pebbles} pebbles left.")
        
        # Switch turns
        turn = -turn

    if turn == -1:
        print("AI wins!")
    else:
        print("Human wins!")

# run game with N pebbles
simulate_game(10)

