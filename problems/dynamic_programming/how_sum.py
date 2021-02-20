def how_sum(target, numbers):
  '''
  Returns an array A of integers (each of which is an element of numbers), such that
  sum(A) == target. Will return only the first such solution, and None if no solution
  exists

  Time complexity:
    - O(n * m^2) since we need to make `n` calls at each recursion depth level, and we
      enter approximately `m` (m=target) number of recursion levels (think about the 
      case of how_sum(target, [1,...]) where we would get [1,...,1] of length `m`)
  
  Space complexity:
    - O(m^2) since we have a memo table with at most `m` keys (m=target), each key
      mapping to a list of length at most `m`

  >>> how_sum(7, [2, 3])
  [2, 2, 3]
  '''
  return _how_sum_recursive(target, numbers, {})

def _how_sum_recursive(target, numbers, memo):
  if target in memo:
    return memo[target]

  if target == 0:
    return []
  
  for num in numbers:
    if target >= num:
      subSolutions = _how_sum_recursive(target - num, numbers, memo)
      if subSolutions is not None:
        memo[target] = [num] + subSolutions
        return memo[target]
  
  memo[target] = None
  return memo[target]

# A few test examples:
print(f'how_sum(7, [2, 3]): {how_sum(7, [2, 3])}') # [2, 2, 3]
print(f'how_sum(7, [2, 4]): {how_sum(7, [2, 4])}') # None
print(f'how_sum(300, [7, 14]): {how_sum(300, [7, 14])}') # None
print(f'how_sum(8, [2, 3, 5]): {how_sum(8, [2, 3, 5])}') # [2, 2, 2, 2]
print(f'how_sum(7, [5, 3, 4, 7]): {how_sum(7, [5, 3, 4, 7])}') # [3, 4]
