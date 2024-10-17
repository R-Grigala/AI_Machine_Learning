from random import choice
from math import inf

# Initialize the game board
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# Function to display the game board
def Gameboard(board):
    chars = {1: 'X', -1: 'O', 0: ' '}
    for row in board:
        for col in row:
            ch = chars[col]
            print(f'| {ch} |', end='')
        print('\n' + '---------------')
    print('===============')

# Function to clear the game board
def Clearboard(board):
    for x, row in enumerate(board):
        for y, col in enumerate(row):
            board[x][y] = 0

# Function to check if a player has won the game
def winningPlayer(board, player):
    conditions = [[board[0][0], board[0][1], board[0][2]],
                  [board[1][0], board[1][1], board[1][2]],
                  [board[2][0], board[2][1], board[2][2]],
                  [board[0][0], board[1][0], board[2][0]],
                  [board[0][1], board[1][1], board[2][1]],
                  [board[0][2], board[1][2], board[2][2]],
                  [board[0][0], board[1][1], board[2][2]],
                  [board[0][2], board[1][1], board[2][0]]]
    return [player, player, player] in conditions

# Function to check if the game has been won
def gameWon(board):
    return winningPlayer(board, 1) or winningPlayer(board, -1)

# Function to print the result of the game
def printResult(board):
    if winningPlayer(board, 1):
        print('X has won! ' + '\n')
    elif winningPlayer(board, -1):
        print('O\'s have won! ' + '\n')
    else:
        print('Draw' + '\n')

# Function to get the list of empty positions on the board
def blanks(board):
    return [[x, y] for x, row in enumerate(board) for y, col in enumerate(row) if col == 0]

# Function to check if the board is full
def boardFull(board):
    return len(blanks(board)) == 0

# Function to set a move on the board for a player
def setMove(board, x, y, player):
    board[x][y] = player

# Minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, alpha, beta, player):
    if gameWon(board) or boardFull(board):
        return [None, None, getScore(board)]
    
    if player == 1:  # Maximizing player (X)
        max_eval = -inf
        best_move = None
        for [x, y] in blanks(board):
            board[x][y] = 1
            eval = minimax(board, depth - 1, alpha, beta, -1)[2]
            board[x][y] = 0  # Undo move

            if eval > max_eval:
                max_eval = eval
                best_move = [x, y]

            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Alpha-Beta pruning
        return [*best_move, max_eval]

    else:  # Minimizing player (O)
        min_eval = inf
        best_move = None
        for [x, y] in blanks(board):
            board[x][y] = -1
            eval = minimax(board, depth - 1, alpha, beta, 1)[2]
            board[x][y] = 0  # Undo move

            if eval < min_eval:
                min_eval = eval
                best_move = [x, y]

            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha-Beta pruning
        return [*best_move, min_eval]

# Function to calculate the score of the current board state
def getScore(board):
    if winningPlayer(board, 1):
        return 10
    elif winningPlayer(board, -1):
        return -10
    else:
        return 0

# Computer's move for 'O' using Minimax
def o_comp(board):
    if len(blanks(board)) == 9:  # Random move for the first turn
        x, y = choice(blanks(board))
    else:
        x, y, _ = minimax(board, len(blanks(board)), -inf, inf, -1)
    setMove(board, x, y, -1)
    Gameboard(board)

# Human player's move
def playerMove(board):
    moves = {1: [0, 0], 2: [0, 1], 3: [0, 2],
             4: [1, 0], 5: [1, 1], 6: [1, 2],
             7: [2, 0], 8: [2, 1], 9: [2, 2]}
    while True:
        try:
            move = int(input('Enter a number between 1-9: '))
            if move < 1 or move > 9 or not (moves[move] in blanks(board)):
                print('Invalid Move! Try again!')
            else:
                setMove(board, moves[move][0], moves[move][1], 1)
                Gameboard(board)
                break
        except(ValueError, KeyError):
            print('Enter a valid number!')

# Game between player and computer
def pvc():
    while True:
        try:
            order = int(input('Enter 1 to go first or 2 to go second: '))
            if order not in [1, 2]:
                print('Invalid Input! Try again!')
            else:
                Gameboard(board)
                break
        except(ValueError, KeyError):
            print('Enter a valid number!')

    while not gameWon(board) and not boardFull(board):
        if order == 1:
            playerMove(board)
            if gameWon(board) or boardFull(board):
                break
            o_comp(board)
        else:
            o_comp(board)
            if gameWon(board) or boardFull(board):
                break
            playerMove(board)

    printResult(board)
    Clearboard(board)

# Main function to start the game
def main():
    while True:
        pvc()
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() == 'no':
            break

# Start the game
if __name__ == '__main__':
    main()
