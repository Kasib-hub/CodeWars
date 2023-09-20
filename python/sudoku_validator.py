# Description: Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board,

# and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells.

# col_grab() and square_grab() are helper functions that check the columns and squares of the board, respectively, for duplicates.
def col_grab(board, col_idx):
    column = set()
    for i in range(9):
        column.add(board[i][col_idx])
    return len(column) == 9

def square_grab(board, row_idx, col_idx):
    square = set()
    for i in range(9):
        for j in range(9):
            if i // 3 == row_idx and j // 3 == col_idx:
                square.add(board[i][j])
    return len(square) == 9

def valid_solution(board):
    for row in range(9):
        # rower is a set of the row
        rower = set(board[row])
        for col in range(9):
            if board[row][col] == 0:
                return False
            
            column = col_grab(board, col)
            square = square_grab(board, row // 3, col // 3)
            if len(rower) != 9 or not column or not square:
                return False
    return True