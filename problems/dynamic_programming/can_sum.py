
def can_sum(target, numbers, memo={}):
  '''
  For a target integer value, and a list of positive integer numbers, returns
  whether or not the target can be achieved by summing a subset (with replacement)
  of numbers

  I.e. Returns True if and only if a subset a_1 * x_1 + ... + a_n * x_n = target
  and a_i is an element of numbers, and x_i is some integer scalar (1 <= i <= n)

  Time complexity:
    - Best: O(1) => can_sum(0, [...]) or can_sum(target, [target,...])
    - Worst: O(n) => no solution, check all subtargets, ex: can_sum(2k-1,[2]) 
      for k >> 1
  
  Space complexity:
    - Best: O(1) => can_sum(0, [...]) or can_sum(target, [target,...])
    - Worst: O(target) => can_sum(target, [1,...]) which requires `target` # of 
      frames on the call stack

  # Below returns True since 3 + 4 = 7 (also 7=7, and 1 * 7 = 7)
  >>> can_sum(7, [5, 3, 4, 7, 1])
  True
  '''
  # We lean on another function as opposed to adding a default optional memo
  # parameter to this function since Python will bind the default memo to the
  # the function definition across subsequent calls!
  return _can_sum_recursive(target, numbers, {})

def _can_sum_recursive(target, numbers, memo):
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

# A few test examples:
print(f'can_sum(0, [1]): {can_sum(0, [1])}')
print(f'can_sum(9, [3]): {can_sum(9, [3])}')
print(f'can_sum(300, [7, 14]): {can_sum(300, [7, 14])}')
print(f'can_sum(7, [2, 4]): {can_sum(7, [2, 4])}')
print(f'can_sum(3, [2, 6, 8, 9]): {can_sum(3, [2, 6, 8, 9])}')
print(f'can_sum(7, [5, 3, 4, 7, 1]): {can_sum(7, [5, 3, 4, 7, 1])}')
print(f'can_sum(12, [1, 2, 6, 8, 9]): {can_sum(12, [1, 2, 6, 8, 9])}')