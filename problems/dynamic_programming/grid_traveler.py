from classes.strategy import Strategy

def grid_traveler(n, m, strategy=Strategy.Tabulation):
  '''
  Given a matrix of dimensions n x m, return the number of ways to
  navigate from the upper left corner of the matrix to the bottom
  right corner using only movements to the right or down
  '''
  if strategy == Strategy.Tabulation:
    return _grid_traveler_tabulative(n, m)
  elif strategy == Strategy.Recursion:
    return _grid_traveler_recursive(n, m, {})

  raise KeyError(f'Invalid strategy: {strategy}')

def _grid_traveler_recursive(n, m, memo):
  '''
  Time complexity: O(n * m)
    * Since we will have at most n * m keys in our memo which limit
      the number of fn calls we will enter. The operations performed
      in each fn call are constant (trivial addition)

  Space complexity: O(n * m)
    * We have n * m keys in our memo which each map to a primitive integer
  '''
  # First base case: an empty matrix
  if n == 0 or m == 0:
    return 0
  
  # Second base case: single cell matrix
  elif n == 1 and m == 1:
    return 1
  
  # If we have a value already computed in the cache, return it
  elif (n,m) in memo:
    return memo[(n,m)]
  # The problem is symmetric about its arguments, so we can return
  # return the reversed args solution if we have it
  elif (m,n) in memo:
    return memo[(m,n)]
  
  # Reduce the problem into two subproblems:
  # (1) The number of solutions after moving right one cell
  # (2) The number of solutions after moving down one cell
  solutionsRightwards = _grid_traveler_recursive(n, m-1, memo)
  solutionsDownwards = _grid_traveler_recursive(n-1, m, memo)

  memo[(n,m)] = solutionsRightwards + solutionsDownwards
  return memo[(n,m)]

def _grid_traveler_tabulative(n, m):
  '''
  Time complexity: O(n * m)
    * We iterate through each cell in our table matrix to find our solution
  
  Space complexity: O(n * m)
    * Our table matrix contains n * m cells each with a primitive integer
  '''

  # Use a table matrix to maintain solutions to subproblems
  # table[i][j] := number of ways to get from the upper left cell
  # to bottom right cell of a matrix of size i x j
  table = [[0] * (m+1) for row in range(n+1)]

  # Base case: A matrix of size 1 x 1 has only the trivial solution
  table[1][1] = 1

  # Induction case: The number of ways to solve a matrix of size
  # i x j is equal to the number of ways to (i-1) x j plus the number
  # of ways for a matrix of size i x (j-1)
  #
  # Put another way, we can traverse through the grid iteratively,
  # adding the number of ways we got to the current cell to both the
  # cell downwards and the cell rightwards
  for row in range(n+1):
    for col in range(m+1):
      if row+1 <= n:
        table[row+1][col] += table[row][col]
      if col+1 <= m:
        table[row][col+1] += table[row][col]
  
  return table[n][m]

for strategy in Strategy:
  assert grid_traveler(1, 1, strategy) == 1
  assert grid_traveler(2, 1, strategy) == 1
  assert grid_traveler(1, 2, strategy) == 1
  assert grid_traveler(2, 2, strategy) == 2
  assert grid_traveler(3, 3, strategy) == 6
  assert grid_traveler(18, 18, strategy) == 2333606220