
from classes.strategy import Strategy

def shifted_binary_search(array, target, strategy=Strategy.Iteration):
  '''
  Given an array of numbers that is sorted but shifted by an unknown number
  of indices in an unknown direction, find and return the first found index of
  the array where array[index] == target.
  
  If target does not exist in the array, returns -1
  '''
  if strategy == Strategy.Iteration:
    return _shifted_binary_search_iterative(array, target)
  elif strategy == Strategy.Recursion:
    return _shifted_binary_search_recursive(array, target, 0, len(array)-1)
  
  raise KeyError(f'Invalid strategy: {strategy}')

def _shifted_binary_search_iterative(array, target):
  left, right = 0, len(array)-1
  while left <= right:

    mid = (left + right) // 2
    leftVal, midVal, rightVal = array[left], array[mid], array[right]

    if midVal == target:
      return mid
    
    # If the left value is less than or equal to the mid value, we know the
    # left half of the current window is in sorted order, so we can tell if we
    # should check the left half or the right half
    elif leftVal <= midVal:
      if leftVal <= target and target < midVal:
        right = mid - 1
      else:
        left = mid + 1

    # Otherwise the right half of the current window is sorted (we know this must be
    # the case since the shift pivot point can only occur in one window or the other)
    else:
      if midVal < target and target <= rightVal:
        left = mid + 1
      else:
        right = mid -1
  
  return -1

def _shifted_binary_search_recursive(array, target, left, right):
  if left > right:
    return -1
  
  mid = (left + right) // 2
  leftVal, midVal, rightVal = array[left], array[mid], array[right]
  if midVal == target:
    return mid
  
  elif leftVal <= midVal:
    if leftVal <= target and target < midVal:
      return _shifted_binary_search_recursive(array, target, left, mid -1)
    else:
      return _shifted_binary_search_recursive(array, target, mid + 1, right)
  
  else:
    if midVal < target and target <= rightVal:
      return _shifted_binary_search_recursive(array, target, mid + 1, right)
    else:
      return _shifted_binary_search_recursive(array, target, left, mid -1)

for strategy in Strategy:
  assert shifted_binary_search([5, 6, 7, 1, 2, 3], 3, strategy) == 5
  assert shifted_binary_search([5, 6, 7, 1, 2, 3], 8, strategy) == -1
  assert shifted_binary_search([130, 133, 99, 100, 110], 133, strategy) == 1
  assert shifted_binary_search([99, 100, 110, 130, 133], 134, strategy) == -1
  assert shifted_binary_search([999, 1000, 64, 81, 144, 256, 512], 81, strategy) == 3
  assert shifted_binary_search([999, 1000, 64, 81, 144, 256, 512], 420, strategy) == -1