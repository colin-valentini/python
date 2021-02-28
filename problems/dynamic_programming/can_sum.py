from classes.strategy import Strategy

def can_sum(target, numbers, strategy=Strategy.Tabulation):
  '''
  For a target integer value, and a list of positive integer numbers, returns
  whether or not the target can be achieved by summing a subset (with replacement)
  of numbers

  I.e. Returns True if and only if a subset a_1 * x_1 + ... + a_n * x_n = target
  and a_i is an element of numbers, and x_i is some integer scalar (1 <= i <= n)

  # Below returns True since 3 + 4 = 7 (also 7=7, and 1 * 7 = 7)
  >>> can_sum(7, [5, 3, 4, 7, 1])
  True
  '''
  if strategy == Strategy.Tabulation:
    return _can_sum_tabulative(target, numbers)
  elif strategy == Strategy.Tabulation:
    return _can_sum_recursive(target, numbers, {})
  
  raise KeyError(f'Invalid strategy: {strategy}')

def _can_sum_recursive(target, numbers, memo):
  '''
  Time complexity: O(n * m) for n = target, m = len(numbers)
    * We make `n` recursive calls in each recursion depth level
      for which we have `m` (m=target) recursive levels in the worst case
      where `numbers` contains 1
  
  Space complexity: O(m) for n = target, m = len(numbers)
    * In the worst case, we're asked to compute can_sum(target, [1,...]) which
      requires m frames on the call stack for stack of branches that reduce by 1
  '''

  # Simplest case (base case): Target is exactly equal to zero
  # in which case we can sum any (or all) elements of numbers zero
  # times to achieve the target
  if target == 0:
    return True
  
  # Lean on our memoization cache to return immediately if answer is
  # already known
  elif target in memo:
    return memo[target]
  
  # Reduce the problem in size: Choose an element of numbers which
  # does not push our target into negative territory, then ask recursively
  # pose the sub-problem of target - num
  for num in numbers:
    if num <= target:
      # If we can achieve the subtarget, we know the solution exists so
      # we can cache it in our memo and return True
      if _can_sum_recursive(target - num, numbers, memo):
        memo[target] = True
        return True

  # If we got here, we did not breaek out early above and should cache False
  # in our memo to prevent redundantly calculating this again
  memo[target] = False  
  return False

def _can_sum_tabulative(target, numbers):
  '''
  Time complexity: O(n * m) for n = target, m = len(numbers)
    * We're uing nested loops, the first with `n` iterations, the second with `m`
  
  Space complexity: O(n) for n = target, m = len(numbers)
    * We have a table array with `n` values
  '''
  # Use a simple array to cache subproblem solutions
  table = [False] * (target + 1)

  # Base case: Always able to construct 0 from any set of numbers (choose none)
  table[0] = True

  # Induction: If any subTarget <= target is constructable, so is 
  # subTarget + num for every num in numbers
  for subTarget in range(target + 1):
    if table[subTarget]:
      for num in numbers:
        superTarget = subTarget + num

        # Guard against attempts out-of-bounds access attempts
        if superTarget <= target:
          table[superTarget] = True

  return table[target]

for strategy in Strategy:
  assert can_sum(0, [1], strategy) == True
  assert can_sum(9, [3], strategy) == True
  assert can_sum(300, [7, 14], strategy) == False
  assert can_sum(7, [2, 4], strategy) == False
  assert can_sum(3, [2, 6, 8, 9], strategy) == False
  assert can_sum(7, [5, 3, 4, 7, 1], strategy) == True
  assert can_sum(12, [1, 2, 6, 8, 9], strategy) == True
