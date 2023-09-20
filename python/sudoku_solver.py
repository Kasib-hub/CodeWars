def column_grab(col_idx, board):
    col = []
    for i in range(9):
        col.append(board[i][col_idx])
    return col
    
def square_grab(row_idx, col_idx, board):
    square = []
    for row in range(9):
        for column in range(9):
            if row // 3 == row_idx and column // 3 == col_idx:
                square.append(board[row][column])
    return square

def is_valid_num(val, row_lst, col_lst, sq_lst):
    if val in row_lst or val in col_lst or val in sq_lst:
        return False
    return True

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""
    for row in range(9):
        for column in range(9):
            
            if puzzle[row][column] == 0:
                row_curr = puzzle[row] # passed row index for the row list
                col_curr = column_grab(column, puzzle) #passed column index
                square = square_grab(row // 3, column // 3, puzzle)
                
                # test all possible numbers for a fit
                for num in range(1, 10):
                    
                    '''
                    Check if valid num by checking the current iteration(num)
                    against the row, column, and square it resides.
                    A valid num is NOT a repeat in those lists.
                    '''
                    if is_valid_num(num, row_curr, col_curr, square):
                        puzzle[row][column] = num

                        # normally I would allow backtracking to continue, but I need to return the solved puzzle before it backtracks further
                        if sudoku(puzzle) is not None:
                            return puzzle
                        
                        # no valid number indicates a backtrack
                        puzzle[row][column] = 0
                return None
    return puzzle