from enum import Enum, auto

def zig_zag_traverse(array):
  '''
  Given a two-dimensional matrix as a list of lists, returns 
  the values in the matrix in "zig zag" ordering (see example).
  - Runs in O(n) time | O(1) space
  
  >>> array = [
    [1,  3,  4, 10],
    [2,  5,  9, 11],
    [6,  8, 12, 15],
    [7, 13, 14, 16],
  ]
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
  '''
  return [value for value in ZigZagMatrix(array)]

class ZigZagMatrix():
  def __init__(self, array):
    self.matrix = array
    self.num_rows = len(array)
    self.num_cols = len(array[0]) if self.num_rows > 0 else 0
  
  def __iter__(self):
    # Begin at the upper left corner of the matrix
    self.row, self.col = 0, 0
    self.direction = self.Direction.DiagonalDown
    return self
  
  def __next__(self):
    if self.row >= self.num_rows and self.col >= self.num_rows:
      raise StopIteration
    
    value = self.matrix[self.row][self.col]
    
    if self._last_cell():
      self.row, self.col = self.row + 1, self.col + 1
    elif self.direction == self.Direction.DiagonalDown:
      self.traverse_below()
    elif self.direction == self.Direction.DiagonalUp:
      self.traverse_above()

    return value

  def traverse_above(self):
    if self.in_bounds(self.row - 1, self.col + 1):
      self.row, self.col = self.row - 1, self.col + 1
      return
    
    self.change_direction()
    if self.in_bounds(self.row, self.col + 1):
      self.col = self.col + 1
    elif self.in_bounds(self.row + 1, self.col):
      self.row = self.row + 1

  def traverse_below(self):
    if self.in_bounds(self.row + 1, self.col - 1):
      self.row, self.col = self.row + 1, self.col - 1
      return
    
    self.change_direction()
    if self.in_bounds(self.row + 1, self.col):
      self.row = self.row + 1
    elif self.in_bounds(self.row, self.col + 1):
      self.col = self.col + 1
  
  def _last_cell(self):
    return self.row == self.num_rows - 1 and self.col == self.num_rows - 1

  def in_bounds(self, row, col):
    return 0 <= row < self.num_rows and 0 <= col < self.num_rows

  def change_direction(self):
    if self.direction == self.Direction.DiagonalUp:
      self.direction = self.Direction.DiagonalDown
    elif self.direction == self.Direction.DiagonalDown:
      self.direction = self.Direction.DiagonalUp
    raise Exception(f'Invalid direction={self.direction}')

  class Direction(Enum):
    DiagonalDown = auto()
    DiagonalUp = auto()

array = [
  [1,  3,  4, 10],
  [2,  5,  9, 11],
  [6,  8, 12, 15],
  [7, 13, 14, 16],
]
assert zig_zag_traverse(array) == [i+1 for i in range(len(array) * len(array[0]))]