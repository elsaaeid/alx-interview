#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys

def is_safe(board, row, col):
    """Check if a queen can be placed
    at the given position
    """
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, board, row=0):
    """Base case: all queens have been placed
    """
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    '''
    Try placing a queen in each column of
    the current row
    '''
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, board, row + 1)

if __name__ == "__main__":
    '''
    Check if the correct number of arguments
    is provided
    '''
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    '''
    Check if N is at least 4
    '''
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(n, board)
