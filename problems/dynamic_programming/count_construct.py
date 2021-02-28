from enum import Enum, auto

class Strategy(Enum):
  Recursion = auto()
  Tabulation = auto()

def count_construct(target, words, strategy=Strategy.Tabulation):
  '''
  Returns the number of ways that the target string can be constructed
  using only words (with replacement) from "words"
  '''
  if strategy == Strategy.Tabulation:
    return _count_construct_tabulative(target, words)
  elif strategy == Strategy.Recursion:
    return _count_construct_recursive(target, words, {})
  
  raise KeyError(f'Invalid strategy: {strategy}')

def _count_construct_recursive(target, words, memo):
  '''
  Time complexity: O(n^2 * m) for n = len(target), m = len(words)
    * Our memoization cache limits the number of branching fn calls to
      just n (since the memo keys are substrings of target such as 
      target[0:], target[1:], target[2:], ..., target[n-1:])
    * For each full fn call, we check each word in words (m of them),
      and each check involves a string comparison operation of length
      at most n => O(n * m) per fn call

  Space complexity: O(n^2)
    * We have a memo with at most n keys, and each k maps to a string of size at most n
  '''
  if len(target) == 0:
    return 1
  elif target in memo:
    return memo[target]
  
  numWays = 0
  for word in words:
    if target.startswith(word):
      subTarget = target[len(word):]
      numWays += _count_construct_recursive(subTarget, words, memo)
  
  memo[target] = numWays
  return numWays

def _count_construct_tabulative(target, words):
  '''
  Time complexity: O(n^2 * m) for n = len(target), m = len(words)
    * We iterate through each subproblem defined by 0,1,...,n
      which requires O(n) iterations
    * Each iteration checks each word in the word bank against the
      rest of the target string (target[i:]) which requires m
      checks, and each check is a string comparison of at most length n
  
  Space complexity: O(n)
    * We maintain a tabular array of size n of subproblem solutions
  '''
  table = [0] * (len(target) + 1)

  # Base case: There is one way to construct target[:0] == ''
  # (by taking no words from the word bank)
  table[0] = 1

  # Induction case: If we can construct a subtarget (target[:i]), 
  # then we can construct part of the rest (target[:i] + word) if
  # the rest of the target (target[i:]) starts with word
  for i in range(len(target)+1):

    # table[i] > 0 <=> target[:i] has some way of being constructed
    if table[i] > 0:
      for word in words:

        # Check if the rest of the target begins with the word, if so
        # we can construct the subTarget + word
        rest = target[i:]
        if rest.startswith(word):
          table[i+len(word)] += table[i]
  
  return table[len(target)]

for strategy in Strategy:
  assert count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], strategy) == 2
  assert count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], strategy) == 1
  assert count_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], strategy) == 0
  assert count_construct("enteratpotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], strategy) == 4
  assert count_construct("e" * 35 + "f", ["e" * i for i in range(1,8)], strategy) == 0
