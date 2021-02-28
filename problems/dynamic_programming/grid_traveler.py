# Given a matrix of dimensions n x m, return the number of ways to
# navigate from the upper left corner of the matrix to the bottom
# right corner using only movements to the right or down
def number_of_ways_to_bottom_right(n, m):
  return get_number_of_ways(n, m, {})

def get_number_of_ways(n, m, memo):
  '''Helper function to recursively break the problem into sub-problems
  and solve with a memoized dynamic programming approach'''
  # First base case: an empty matrix
  if n == 0 or m == 0:
    return 0
  
  # Second base case: single cell matrix
  if n == 1 and m == 1:
    return 1
  
  # If we have a value already computed in the cache, return it
  if (n,m) in memo:
    return memo[(n,m)]
  # The problem is symmetric about its arguments, so we can return
  # return the reversed args solution if we have it
  elif (m,n) in memo:
    return memo[(m,n)]
  
  # Reduce the problem into two subproblems:
  # (1) The number of solutions after moving right one cell
  # (2) The number of solutions after moving down one cell
  memo[(n,m)] = get_number_of_ways(n, m-1, memo) + get_number_of_ways(n-1, m, memo)
  return memo[(n,m)]

assert number_of_ways_to_bottom_right(18, 18) == 2333606220