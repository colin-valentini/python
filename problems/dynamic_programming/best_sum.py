from enum import Enum, auto

class Strategy(Enum):
  Recursion = auto()
  Tabulation = auto()

def best_sum(target, numbers, strategy=Strategy.Tabulation):
  '''
  Returns an array A of integers (each of which is an element of `numbers`), such that
  `sum(A) == target`, and `len(A)` is minimal across all possibe solutions `A`

  If no solution exists, returns None

  >>> best_sum(300, [1, 10, 30, 50])
  [100, 100, 100]

  >>> best_sum(300, [1, 25, 50, 150])
  [150, 150]
  '''
  if strategy == Strategy.Tabulation:
    return _best_sum_tabulative(target, numbers)
  elif strategy == Strategy.Recursion:
    return _best_sum_recursive(target, numbers, {})
  
  raise KeyError(f'Invalid strategy: {strategy}')

def _best_sum_recursive(target, numbers, memo):
  '''
  Time complexity: O(n^2 * m) for n = target, m = len(numbers)
    * Worst case recursion causes n levels deep (1, ..., 1 n times) => O(n)
    * Each recursive level could branch out to at most m additional nodes => O(n * m)
    * Each function call requires copying an array into our memo of size at most n => O(n * m * n)
  
  Space complexity:
    - O(n^2) since:
      * We are maintaing a memo cache with at most n number of keys, and
      * Each key in the memo cache contains an array of at most n length
  '''
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

def _best_sum_tabulative(target, numbers):
  '''
  Time complexity: O(n^2 * m) for n = target, m = len(numbers)
    * 

  Space complexity: O(n^2)
  '''
  table = [None] * (target + 1)

  # Base case: The best way to construct zero is with no elements from numbers
  table[0] = []

  # Induction case: If we can construct a subTarget <= target amount, then
  # we an also construct a solution for subTarget + num for each num in numbers
  # (maintain only the minimum length solutions as we go)
  for subTarget in range(target+1):

    # If the subproblem has a solution, then we can continue
    if table[subTarget] is not None:
      for num in numbers:
        superTarget = subTarget + num
        if superTarget <= target:

          # If there's already a supertarget solution, we compare
          # the current solution to the alternative of using the 
          # subtarget's solution + [num], choosing the shorter of the two
          candidate = table[subTarget] + [num]
          if table[superTarget] is not None:
            if len(candidate) < len(table[superTarget]):
              table[superTarget] = candidate

          # Otherwise set the supertarget's solution array to the just
          # found solution (candidate)
          else:
            table[superTarget] = candidate
    
  return table[target]

# Some test examples
assert best_sum(8, [2, 3, 5]) == [3, 5]
assert best_sum(7, [1, 2, 3]) == [1, 3, 3]
assert best_sum(100, [1, 2, 5, 25, 8]) == [25, 25, 25, 25]
assert best_sum(300, [1, 10, 30, 50, 100]) == [100, 100, 100]