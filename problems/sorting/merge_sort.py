def merge_sort(array):
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
  return merge_sorted_arrays(merge_sort(left), merge_sort(right))

def merge_sorted_arrays(left, right):
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
  result = merge_sort(test_case.copy())
  expected = sorted(test_case)
  assert result == expected