from classes.strategy import Strategy

def how_sum(target, numbers, strategy=Strategy.Tabulation):
  '''
  Returns an array A of integers (each of which is an element of numbers), such that
  sum(A) == target. Will return only the first such solution, and None if no solution
  exists

  >>> how_sum(7, [2, 3])
  [2, 2, 3]
  '''
  if strategy == Strategy.Tabulation:
    return _how_sum_tabulative(target, numbers)
  elif strategy == Strategy.Recursion:
    return _how_sum_recursive(target, numbers, {})
  
  raise KeyError(f'Invalid strategy: {strategy}')

def _how_sum_recursive(target, numbers, memo):
  '''
  Time complexity: O(n^2 * m) for n = target, m = len(numbers)
    * Since we need to make n calls at each recursion depth level, and we
      enter approximately m (m=target) number of recursion levels (think about the 
      case of how_sum(target, [1,...]) where we would get [1,...,1] of length n)
  
  Space complexity: O(n ^ 2)
    * Since we have a memo table with at most n keys, each key mapping to a 
      list of length at most n
  '''
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

def _how_sum_tabulative(target, numbers):
  '''
  Time complexity: O(n^2 * m) for n = target, m = len(numbers)
    * We have nested for loops, the first with n iterations, and the second
      with at most m iterations
    * Each iteration of the loop could require an array copy operation on an
      array of size at most n
  
  Space complexity: O(n^2)
    * We maintain a tabulation array of size n to cache intermediate results
    * The tabulation array elements are arrays of size at most n
  '''
  # Initialize a table array filled with the value return if no solution exists
  table = [None] * (target + 1)

  # Base case: A target of zero can always be constructed by using no numbers
  table[0] = []

  # Induction case: If a subTarget <= target is constructable, then so is
  # subTarget + num for each num in numbers
  for subTarget in range(target+1):
    if table[subTarget] is not None:
      for num in numbers:
        superTarget = subTarget + num
        # Copy over the list of solution values from the subproblem (subTarget)
        # append the current num to that list. Push this into the table
        # as the solution to the superproblem (superTarget)
        #
        # Small optimization: only proceed to do this if we haven't already found
        # a solution to the superproblem (since we only need to return one solution)
        if superTarget <= target and table[superTarget] is None:
          table[superTarget] = table[subTarget] + [num]
  
  return table[target]

# A few test examples:
assert sum(how_sum(7, [2, 3])) == 7
assert how_sum(7, [2, 4]) is None
assert how_sum(300, [7, 14]) is None
assert sum(how_sum(8, [2, 3, 5])) == 8
assert sum(how_sum(7, [5, 3, 4, 7])) == 7
