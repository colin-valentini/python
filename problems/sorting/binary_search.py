
from classes.strategy import Strategy

def binary_search(array, target, strategy=Strategy.Iteration, validate_sorted=False):
  '''
  The prototypical binary search algorithm implemented at a high level with the ability
  to toggle between iterative or recursive strategy

  O(log(n)) time | O(1) space
  '''
  if validate_sorted:
    if not _array_is_sorted(array):
      raise Exception('Input <array> is not in sorted order')
  
  # Small shortcut if the target is completely out of the array's range, or the
  # array itself is completely empty. NOTE: We return -1 if the array is empty
  # to match Python's built-in `in` operator behavior where `1 in []` returns
  # the not found value, but doesn't raise an exception
  if not len(array) or target < array[0] or array[-1] < target:
    return -1

  if strategy == Strategy.Iteration:
    return _binary_search_iterative(array, target)
  elif strategy == Strategy.Recursion:
    return _binary_search_recursive(array, target, 0, len(array)-1)
  
  raise KeyError(f'Invalid strategy: {strategy}')  

def _binary_search_iterative(array, target):
  # Create a window from the start index of the array to the last index,
  # keep searching windows of halving size until we find the array or
  # our window becomes smaller than size 1
  left, right = 0, len(array)-1
  while left <= right:

    mid = (left + right) // 2
    leftVal, midVal, rightVal = array[left], array[mid], array[right]

    # If the midpoint is exaclty our target, we're done
    if midVal == target:
      return mid
    
    # Since the array is sorted we can simply check the left half if the
    # target is less than our midpoint value. Do this by moving the right
    # pointer to just left of the mid pointer
    elif target < midVal:
      right = mid - 1
    
    # If the target value is greater than our midpoint value, search the
    # right half by moving the left pointer to just after the mid pointer
    #
    # NOTE: We don't need a strict else, since the target can only be equal,
    # smaller, or greater than our mid value (so this is effectively an else
    # with better readability)
    elif midVal < target:
      left = mid + 1
  
  # The standard 'not found' indicator value is -1 since -1 is not a valid index
  return -1

def _binary_search_recursive(array, target, left, right):
  if left > right:
    return -1
  
  mid = (left + right) // 2
  leftVal, midVal, rightVal = array[left], array[mid], array[right]
  if midVal == target:
    return mid
  elif target < midVal:
    return _binary_search_recursive(array, target, left, mid-1)
  elif midVal < target:
    return _binary_search_recursive(array, target, mid+1, right)

def _array_is_sorted(array):
  '''
  An O(n) scan across the array to check if the array is sorted
  '''
  return all(map(lambda i: array[i-1] <= array[i], range(1,len(array))))

for strategy in Strategy:
  assert binary_search([1,2,3,4,5,6,7], 3, strategy) == 2
  assert binary_search([1,2,3,4,5,6,7], 8, strategy) == -1
  assert binary_search([99, 100, 110, 130, 133], 133, strategy) == 4
  assert binary_search([99, 100, 110, 130, 133], 134, strategy) == -1
  assert binary_search([64, 81, 144, 256, 512], 81, strategy) == 1
  assert binary_search([64, 81, 144, 256, 512], 420, strategy) == -1