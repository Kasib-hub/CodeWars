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
        rower = set(board[row])
        for col in range(9):
            if board[row][col] == 0:
                return False
            
            column = col_grab(board, col)
            square = square_grab(board, row // 3, col // 3)
            if len(rower) != 9 or not column or not square:
                return False
    return True