def best_sum(target, numbers):
  '''
  Returns an array A of integers (each of which is an element of `numbers`), such that
  `sum(A) == target`, and `len(A)` is minimal across all possibe solutions `A`

  If no solution exists, returns None

  Time complexity:
    - O(n*m^2) since:
      * We will have at worst `m` (m=target) recursion levels deep => O(m)
      * At each recursive level could at most branch out to `n` additional nodes => O(m * n)
        (we don't have to fully drill into every sub-branch completely due to our memo)
      * For each function call we have to update our memo with an array at each => O(m * n * m)
  
  Space complexity:
    - O(m^2) since:
      * We are maintaing a memo cache with at most `m` (m=target) number of keys, and
      * Each key in the memo cache contains an array of at most `m` length

  >>> best_sum(300, [1, 10, 30, 50])
  [100, 100, 100]

  >>> best_sum(300, [1, 25, 50, 150])
  [150, 150]
  '''
  return _best_sum_recursive(target, numbers, {})

def _best_sum_recursive(target, numbers, memo):
  if target == 0:
    return []
  
  elif target in memo:
    return memo[target]
  
  solution = None
  for num in numbers:
    if num <= target:
      subSolution = _best_sum_recursive(target - num, numbers, memo)

      # If we found valid solutions to the subProblem
      if subSolution is not None:

        # Only update our current global best if this subSolution is shorter in length
        if solution is not None:
          solution = [num]+subSolution if len(subSolution)+1 < len(solution) else solution
        else:
          solution = [num]+subSolution
  
  memo[target] = solution
  return memo[target]

# Some test examples
print(f'best_sum(8, [2, 3, 5]): {best_sum(8, [2, 3, 5])}') # [3, 5]
print(f'best_sum(7, [1, 2, 3]): {best_sum(7, [1, 2, 3])}') # [1, 3, 3]
print(f'best_sum(300, [1, 10, 30, 50, 100]): {best_sum(300, [1, 10, 30, 50, 100])}') # [100, 100, 100]