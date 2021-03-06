
def quick_sort(array):
  '''
  Prototypical quick sort algorithm using Python

  Time and Space Complexity:
    * Best: O(n * log(n)) time | O(log(n)) space
    * Avg: O(n * log(n)) time | O(log(n)) space
    * Worst: O(n^2) time | O(log(n)) space
  '''
  return _quick_sort(array, 0, len(array)-1)

def _quick_sort(array, start, end):
  # We don't need to sort an array of size 1 (already sorted), or less
  if start >= end:
    return

  pivot = partition(array, start, end)
  _quick_sort(array, start, pivot-1)
  _quick_sort(array, pivot+1, end)

def partition(array, start, end):
  pivot, pivotVal = start, array[start]
  left, right = start+1, end

  while left <= right:
    if array[left] > pivotVal and array[right] < pivotVal:
      swap(array, left, right)
    if array[left] <= pivotVal:
      left += 1
    if pivotVal <= array[right]:
      right -= 1
  
  swap(array, pivot, right)
  return right

def swap(array, i, j):
  '''
  Swaps the value at the i-th index with the value at the j-th index in place.
  '''
  if i < 0 or i > len(array)-1:
    raise IndexError(f'Index <i> of {i} is not a valid index of <array>')
  elif j < 0 or j > len(array)-1:
    raise IndexError(f'Index <j> of {j} is not a valid index of <array>')
  elif i == j:
    return
  
  array[i], array[j] = array[j], array[i]
  

test_cases = [
  [],
  [3,2],
  [2,3,1],
  [1,2,3],
  [33, 33, 33, 33, 33],
  [33, 33, 33, 33, 44],
  [16, 1, 53, 99, 16, 9, 100, 300, 12],
]

for test_case in test_cases:
  result = test_case.copy()
  quick_sort(result)
  assert result == sorted(test_case)