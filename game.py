import numpy as np
import sys
import math
from board import *

# Initialize the game state
board = np.zeros((NUM_ROWS, NUM_COLS))  # Empty game board
current_player = 1  # Player 1 starts the game

def is_valid_move(column):
    """Check if a move is valid in the given column."""
    return board[NUM_ROWS-1][column] == 0

def make_move(column):
    """Make a move in the given column."""
    for row in range(NUM_ROWS):
        if board[row][column] == 0:
            board[row][column] = current_player
            return row, column

def check_win(row, column):
    """Check if the current move resulted in a win."""
    # Check horizontal
    for c in range(NUM_COLS - 3):
        if board[row][c] == current_player and board[row][c+1] == current_player and board[row][c+2] == current_player and board[row][c+3] == current_player:
            return True

    # Check vertical
    for r in range(NUM_ROWS - 3):
        if board[r][column] == current_player and board[r+1][column] == current_player and board[r+2][column] == current_player and board[r+3][column] == current_player:
            return True

    # Check diagonal (top-left to bottom-right)
    for r in range(NUM_ROWS - 3):
        for c in range(NUM_COLS - 3):
            if board[r][c] == current_player and board[r+1][c+1] == current_player and board[r+2][c+2] == current_player and board[r+3][c+3] == current_player:
                return True

    # Check diagonal (top-right to bottom-left)
    for r in range(NUM_ROWS - 3):
        for c in range(3, NUM_COLS):
            if board[r][c] == current_player and board[r+1][c-1] == current_player and board[r+2][c-2] == current_player and board[r+3][c-3] == current_player:
                return True

    return False

def switch_player():
    """Switch the current player."""
    global current_player
    current_player = 2 if current_player == 1 else 1

# Main game loop
while True:
    # Draw the current game state
    draw_board()

    # Prompt the current player for a move
    column = int(input(f"Player {current_player}, choose a column (0-{NUM_COLS-1}): "))

    # Validate the move
    if not 0 <= column < NUM_COLS:
        print("Invalid column. Try again.")
        continue

    if not is_valid_move(column):
        print("Column is full. Try again.")
        continue

    # Make the move
    row, col = make_move(column)

    # Check for a win
    if check_win(row, col):
        draw_board(board)
        print(f"Player {current_player} wins!")
        sys.exit()

    # Check for a draw
    if np.count_nonzero(board) == NUM_ROWS * NUM_COLS:
        draw_board(board)
        print("It's a draw!")
        sys.exit()

    # Switch to the next player
    switch_player()
