from enum import Enum, auto

def search_for_range(array, target):
  '''
  Given an array of sorted integers and a target integer, returns an
  index range within which the target is contained.

  Runs in O(log(n)) time | O(1) space
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
    self._check_direction(direction)

    while left <= right:
      mid = (left + right) // 2

      # Standard binary search protocol
      if self.target < self.array[mid]:
        right = mid - 1
      elif self.target > self.array[mid]:
        left = mid + 1

      # In the event that we find a match at the middle index, only search the window 
      # in the direction specified
      else:
        # (1) Searching left window
        if direction == self.SearchDirection.Left:
          if mid > self.MIN_INDEX and self.array[mid - 1] == self.target:
            right = mid - 1
          else:
            self.range_lower = mid
            return
        
        # (2) Searching right window
        elif direction == self.SearchDirection.Right:
          if mid < self.MAX_INDEX and self.array[mid + 1] == self.target:
            left = mid + 1
          else:
            self.range_upper = mid
            return

  class SearchDirection(Enum):
    Left = auto()
    Right = auto()

  def _check_direction(self, direction):
    if direction != self.SearchDirection.Left and direction != self.SearchDirection.Right:
      raise Exception(f'Invalid search direction: {direction}')

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