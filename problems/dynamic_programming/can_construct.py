def can_construct(target, words):
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
  return _can_construct_recursive(target, words, {})

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

# Some test examples
print(f'can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]): {can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"])}') # True
print(f'can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]): {can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])}') # False
print(f'can_construct("e" * 35 + "f", ["e" * i for i in range(1,8)]): {can_construct("e" * 35 + "f", ["e" * i for i in range(1,8)])}') # False