from enum import Enum, auto

def search_for_range(array, target):
  '''
  Given an array of sorted integers and a target integer, returns an
  index range within which the target is contained.

  Runs in O(log(n)) time | O(log(n)) space
  '''
  return RangeFinder(array, target).target_range()

class RangeFinder():
  def __init__(self, array, target):
    self.array = array
    self.target = target
    self.MIN_INDEX = 0
    self.MAX_INDEX = len(self.array) - 1
    self.NOT_FOUND = -1
  
  def target_range(self):
    self.range_lower, self.range_upper = self.NOT_FOUND, self.NOT_FOUND
    self._binary_search(self.MIN_INDEX, self.MAX_INDEX, self.SearchDirection.Left)
    self._binary_search(self.MIN_INDEX, self.MAX_INDEX, self.SearchDirection.Right)
    return self.range_lower, self.range_upper
  
  def _binary_search(self, left, right, direction):
    if direction != self.SearchDirection.Left and direction != self.SearchDirection.Right:
      raise Exception(f'Invalid search direction: {direction}')
    
    # Base case: have completely searched through
    if left > right:
      return
    
    # Recursive case: binary search this window
    mid = (left + right) // 2

    # Standard binary search protocol
    if self.target < self.array[mid]:
      self._binary_search(left, mid - 1, direction)
    elif self.target > self.array[mid]:
      self._binary_search(mid + 1, right, direction)

    # In the event that we find a match at the middle index, only search the window 
    # in the direction specified
    else:
      # (1) Searching left window
      if direction == self.SearchDirection.Left:
        if mid > self.MIN_INDEX and self.array[mid - 1] == self.target:
          self._binary_search(left, mid - 1, direction)
        else:
          self.range_lower = mid
      # (2) Searching right window
      elif direction == self.SearchDirection.Right:
        if mid < self.MAX_INDEX and self.array[mid + 1] == self.target:
          self._binary_search(mid + 1, right, direction)
        else:
          self.range_upper = mid

  class SearchDirection(Enum):
    Left = auto()
    Right = auto()

# Test cases
assert search_for_range([5, 7, 7, 8, 8, 10], 5) == (0,0)
assert search_for_range([5, 7, 7, 8, 8, 10], 7) == (1,2)
assert search_for_range([5, 7, 7, 8, 8, 10], 8) == (3,4)
assert search_for_range([5, 7, 7, 8, 8, 10], 10) == (5,5)
assert search_for_range([5, 7, 7, 8, 8, 10], 9) == (-1,-1)
assert search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 45) == (4,9)
assert search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 45, 45, 45], 45) == (4,12)
assert search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], 47) == (-1,-1)
assert search_for_range([0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73], -1) == (-1,-1)