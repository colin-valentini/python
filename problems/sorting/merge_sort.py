from enum import Enum, auto

class Strategy(Enum):
  Optimal = auto()
  Simple = auto()

def merge_sort(array, strategy=Strategy.Optimal):
  if strategy == Strategy.Optimal:
    return _merge_sort_optimal(array)
  elif strategy == Strategy.Simple:
    return _merge_sort_simple(array)
  raise KeyError(f'Invalid strategy: {strategy}') 

def _merge_sort_optimal(array):
  '''
  Space optimized merge sort algorithm which performs the sorting in place.
   - O(n*log(n)) time | O(n) space
  '''
  _merge_sort_in_place(array, array.copy(), 0, len(array)-1)
  return array

def _merge_sort_in_place(main, auxiliary, start, stop):
  # Base case: array of length zero or one is trivially sorted in place
  if start >= stop:
    return
  
  mid = (start + stop) // 2
  _merge_sort_in_place(auxiliary, main, start, mid)
  _merge_sort_in_place(auxiliary, main, mid+1, stop)
  _do_merge_in_place(main, auxiliary, start, mid, stop)

def _do_merge_in_place(main, auxiliary, start, mid, stop):
  i, j, k = start, mid + 1, start
  while i <= mid and j <= stop:
    if auxiliary[i] <= auxiliary[j]:
      main[k] = auxiliary[i]
      i += 1
    else:
      main[k] = auxiliary[j]
      j += 1
    k += 1
  
  while i <= mid:
    main[k] = auxiliary[i]
    i, k = i + 1, k + 1
  while j <= stop:
    main[k] = auxiliary[j]
    j, k = j + 1, k + 1

def _merge_sort_simple(array):
  '''
  Simple implementation of the merge sort algorithm which is not
  optimized for space. Sorting is NOT done in place!
   - O(n*log(n)) time | O(n*log(n)) space
  '''
  # Our base case is the trivially sorted zero or one length array
  if len(array) <= 1:
    return array
  
  mid = len(array) // 2
  left, right = array[:mid], array[mid:]

  # Recursive calls all resolve to sorted sub-arrays of left and right
  # so we just need to merge them and return
  return _do_merge_simple(_merge_sort_simple(left), _merge_sort_simple(right))

def _do_merge_simple(left, right):
  i, j = 0, 0
  merged_array = []
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      merged_array.append(left[i])
      i += 1
    else:
      merged_array.append(right[j])
      j += 1
  
  # Because the above while loop terminates as soon as one of the pointers
  # exceeds the length of it's array, we need to extend the other values
  # into our merged_array. These values are obviously all larger than all
  # other values currently captured so a simple extend is sufficient
  if i < len(left):
    merged_array.extend(left[i:])
  elif j < len(right):
    merged_array.extend(right[j:])
  
  return merged_array

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
  for strategy in Strategy:
    result = merge_sort(test_case.copy(), strategy)
    expected = sorted(test_case)
    assert result == expected