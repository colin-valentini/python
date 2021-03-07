import math

def sudoku_solver(sudoku_board):
  '''
  Given a 9x9 partially filled sudoku board, returns the solution board (if it exists).
  The given sudoku board is a square matrix (list of lists) where each value is
  in 0-9, with 0 values indicating an empty space.

  sudoku_board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
  ]
  >>> sudoku_solver(sudoku_board)
  True

  >>> print(sudoku_board)
  [
    [7, 8, 5, 4, 3, 9, 1, 2, 6],
    [6, 1, 2, 8, 7, 5, 3, 4, 9],
    [4, 9, 3, 6, 2, 1, 5, 7, 8],
    [8, 5, 7, 9, 4, 3, 2, 6, 1],
    [2, 6, 1, 7, 5, 8, 9, 3, 4],
    [9, 3, 4, 1, 6, 2, 7, 8, 5],
    [5, 7, 8, 3, 9, 4, 6, 1, 2],
    [1, 2, 6, 5, 8, 7, 4, 9, 3],
    [3, 4, 9, 2, 1, 6, 8, 5, 7],
  ]
  '''
  if len(sudoku_board) != len(sudoku_board[0]):
    raise TypeError('Argument <sudoku_board> must be a square matrix')
  elif len(sudoku_board) != 9:
    raise TypeError('Argument <sudoku_board> must be a matrix of size 9x9')

  if _partial_sudoku_solver(sudoku_board, 0, 0):
    return sudoku_board
  else:
    raise Exception('No solution found for the given sudoku board')

def _partial_sudoku_solver(sudoku_board, row, col):
  '''
  A backtracking algorithm to solve a sudoku board from the given
  position (row and column). If this cell is unfilled, we try different
  values for it, and continue searching only for valid values.

  If no valid solutions exist, we return False (via the inner _try_values
  function call), otherwise we fill the board in place and return True.
  '''
  # If the provided column index is beyond the boundary, we
  # move the cell position to the first element of the next line
  if col == len(sudoku_board):
    row, col = row + 1, 0

    # If we've overflowed our row boundary we know that we've visited and
    # embedded a value in every other unfilled cell in the board => done
    if row == len(sudoku_board):
      return True
  
  # If the current cell is not filled, we can do a backtracking search
  # to try different possible values at this position. We can return the
  # result of the search (True/False) for propagation
  if not sudoku_board[row][col]:
    return _try_values_at_cell(row, col, sudoku_board)
  
  # If the current cell is filled already, we don't have to try anything
  # here (no choices for us) so we proceed to the next cell
  return _partial_sudoku_solver(sudoku_board, row, col + 1)

def _try_values_at_cell(row, col, sudoku_board):
  for digit in range(1,10):
    if _is_valid_cell_value(digit, row, col, sudoku_board):
      sudoku_board[row][col] = digit
      if _partial_sudoku_solver(sudoku_board, row, col + 1):
        return True
  
  sudoku_board[row][col] = 0
  return False

def _is_valid_cell_value(value, row, col, sudoku_board):
  '''Returns True if <value> is valid for the cell at position (<row>,<col>)
  in the given sudoku board matrix'''

  # (1) Check if value already exists in row
  if value in sudoku_board[row]:
    return False
  
  # (2) Check if value already exists in column
  if value in map(lambda r: r[col], sudoku_board):
    return False
  
  # (3) Check if value already exists in the subgrid
  subgridRows, subgridCols = _get_subgrid_range_of_cell(row, col, sudoku_board)
  for r in subgridRows:
    for c in subgridCols:
      if sudoku_board[r][c] == value:
        return False
  
  # Reaching the end means we failed to invalidate this cell, so it must be valid
  return True

def _get_subgrid_range_of_cell(row, col, sudoku_board):
  '''Returns the row index range and column index range (as a tuple pair) that define
  the subgrid for the given cell (sudoku boards are square boards with subgrids)
  '''
  dimension = int(math.sqrt(len(sudoku_board)))
  rowStart = (row // dimension ) * dimension
  colStart = (col // dimension) * dimension
  return range(rowStart, rowStart + dimension), range(colStart, colStart + dimension)

sudoku_board = [
  [7, 8, 0, 4, 0, 0, 1, 2, 0],
  [6, 0, 0, 0, 7, 5, 0, 0, 9],
  [0, 0, 0, 6, 0, 1, 0, 7, 8],
  [0, 0, 7, 0, 4, 0, 2, 6, 0],
  [0, 0, 1, 0, 5, 0, 9, 3, 0],
  [9, 0, 4, 0, 6, 0, 0, 0, 5],
  [0, 7, 0, 3, 0, 0, 0, 1, 2],
  [1, 2, 0, 0, 0, 7, 4, 0, 0],
  [0, 4, 9, 2, 0, 6, 0, 0, 7],
]
assert sudoku_solver(sudoku_board)
assert sudoku_board == [
  [7, 8, 5, 4, 3, 9, 1, 2, 6],
  [6, 1, 2, 8, 7, 5, 3, 4, 9],
  [4, 9, 3, 6, 2, 1, 5, 7, 8],
  [8, 5, 7, 9, 4, 3, 2, 6, 1],
  [2, 6, 1, 7, 5, 8, 9, 3, 4],
  [9, 3, 4, 1, 6, 2, 7, 8, 5],
  [5, 7, 8, 3, 9, 4, 6, 1, 2],
  [1, 2, 6, 5, 8, 7, 4, 9, 3],
  [3, 4, 9, 2, 1, 6, 8, 5, 7],
]

sudoku_board = [
  [0, 0, 0, 0, 3, 0, 0, 0, 9],
  [0, 4, 0, 5, 0, 0, 0, 7, 8],
  [2, 9, 0, 0, 0, 1, 0, 5, 0],
  [0, 7, 8, 0, 0, 3, 0, 0, 6],
  [0, 3, 0, 0, 6, 0, 0, 8, 0],
  [6, 0, 0, 8, 0, 0, 9, 3, 0],
  [0, 6, 0, 9, 0, 0, 0, 2, 7],
  [7, 2, 0, 0, 0, 5, 0, 6, 0],
  [8, 0, 0, 0, 7, 0, 0, 0, 0]
]
assert sudoku_solver(sudoku_board)
assert sudoku_board = [
  [1, 8, 5, 7, 3, 6, 2, 4, 9],
  [3, 4, 6, 5, 2, 9, 1, 7, 8],
  [2, 9, 7, 4, 8, 1, 6, 5, 3],
  [5, 7, 8, 2, 9, 3, 4, 1, 6],
  [9, 3, 2, 1, 6, 4, 7, 8, 5],
  [6, 1, 4, 8, 5, 7, 9, 3, 2],
  [4, 6, 3, 9, 1, 8, 5, 2, 7],
  [7, 2, 9, 3, 4, 5, 8, 6, 1],
  [8, 5, 1, 6, 7, 2, 3, 9, 4]
]