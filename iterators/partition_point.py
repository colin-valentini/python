
def partition_point(arr, predicate):
  '''
  Takes a list of values and partitions the list such that all the 
  values satisfying the predicate condition are on the left of the
  array, and all the values not satisfying the predicate condition
  are on the right of the array.

  Function returns the index where values become False according to 
  the predicate.
  '''
  lo, hi = 0, len(arr)
  while lo < hi:
    mid = (lo + hi) // 2
    if predicate(mid, arr[mid], arr):
      lo = mid + 1
    else:
      hi = mid
  return lo

print(partition_point([0, 0, 1, 1, 1, 1], lambda index, val, arr: val == 0))