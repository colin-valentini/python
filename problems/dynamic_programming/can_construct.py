from enum import Enum, auto

class Strategy(Enum):
  Recursion = auto()
  Tabulation = auto()

def can_construct(target, words, strategy=Strategy.Tabulation):
  '''
  Returns a bool value representing whether or not the given `target` string can be
  constructed using only words from the list `words` (with replacement)

  Time complexity:
    - O(n^2 * m) since:
      * Because we're using a memoization cache, we will only ever visit each subtarget
        once (each subtarget is a consecutive substring of target), and there are 
        exactly `n` such substrings (so `n` keys in our memo in worst case)
      * Each fn call has to also construct a substring (which is an "array copy"-like 
        operation) which takes O(n)
      * Each recursive call branches at most `m` times (for m = len(words))
  
  Space complexity:
    - O(n^2) since:
      * 
  '''
  if strategy == Strategy.Tabulation:
    return _can_construct_tabulative(target, words)
  elif strategy == Strategy.Recursion:
    return _can_construct_recursive(target, words, {})
  
  raise KeyError(f'Invalid strategy: {strategy}')

def _can_construct_recursive(target, words, memo):

  if not len(target):
    return True
  elif target in memo:
    return memo[target]
  
  for word in words:
    if target.startswith(word):
      subTarget = target[len(word):]
      if _can_construct_recursive(subTarget, words, memo):
        return True
  
  memo[target] = False
  return memo[target]

def _can_construct_tabulative(target, words):
  '''
  Time complexity: O(n^2 * m) for n = len(target), m = len(words)
    * We check each consecutive substring (target[:0], target[:1],...,target[:i])
      and check if target[:i] starts with one of our words which requires O(m)
      checks per iteration, with a total of O(n) iterations
    * We are also doing string character comparisons when we check if a word 
      matches the prefix of our subtarget, which requires at most n comparisons

  Space complexity: O(n)
    * We use a tabular array of size n to maintain solutions to subproblems
  '''
  # Use a table array to maintain solutions to subproblems, in this setup
  # each value 'i' in the table corresponds to whether target[:i] 
  # can be constructed using just elements from "words"
  #
  # Ex: target='hello', table[2] == True => 'el' (target[:2]) can be 
  # constructed from elements of "words"
  table = [False] * (len(target) + 1)
  
  # Base case: Empty string == target[:0], which is always constructable
  table[0] = True

  # Induction case: If we can construct a subTarget (subTarget is a prefix
  # of target), then we can construct subTarget + word for each word in words
  for i in range(len(target)+1):
    # If the current position is reachable, we know we appending a word from
    # the word bank is also reachable
    if table[i]:
      for word in words:

        # target[0:] = 'abcdef'
        # target[1:] = 'bcdef'
        # target[2:] = 'cdef'
        # ...
        # target[N:] = ''
        rest = target[i:]
        if rest.startswith(word):
          table[i+len(word)] = True

  return table[len(target)]

for strategy in Strategy:
  assert can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], strategy) == True
  assert can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"], strategy) == True
  assert can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"], strategy) == False
  assert can_construct("enteratpotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], strategy) == True
  assert can_construct("e" * 35 + "f", ["e" * i for i in range(1,8)], strategy) == False