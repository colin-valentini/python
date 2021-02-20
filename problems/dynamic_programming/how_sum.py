def how_sum(target, numbers):
  '''
  Returns an array A of integers (each of which is an element of numbers), such that
  sum(A) == target. Will return only the first such solution, and None if no solution
  exists
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
        subSolutions.append(num)
        memo[target] = subSolutions
        return memo[target]
  
  memo[target] = None
  return memo[target]

# A few test examples:
print(f'how_sum(7, [2, 3]): {how_sum(7, [2, 3])}') # [2, 2, 3]
print(f'how_sum(7, [2, 4]): {how_sum(7, [2, 4])}') # None
print(f'how_sum(300, [7, 14]): {how_sum(300, [7, 14])}') # None
print(f'how_sum(7, [5, 3, 4, 7]): {how_sum(7, [5, 3, 4, 7])}') # [4, 3]
print(f'how_sum(8, [2, 3, 5]): {how_sum(8, [2, 3, 5])}') # [2, 2, 2, 2]
