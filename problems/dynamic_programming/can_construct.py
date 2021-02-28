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
  return _can_construct_tabulative(target, words)

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
  Time complexity: O() for n = len(target), m = len(words)
    * 

  Space complexity: O()
  '''
  # Use a table array to maintain solutions to subproblems, in this setup
  # each value 'i' in the table corresponds to whether target[len(target)-i:] 
  # can be constructed using just string from "words"
  #
  # Ex: target='hello', table[4] == True => 'ello' (target[5-4:]) can be 
  # constructed from elements of "words"
  table = [False] * (len(target) + 1)
  
  # Base case: Empty string
  table[0] = True

  # Induction case: If we can construct a subTarget (subTarget is a substring
  # of target), then we can construct word + subTarget
  for i in range(len(target)+1):
    subTarget = target[len(target)-i:]
    if table[i]:
      for word in words:

        # Check if adding this word to the substring creates a match with
        # the target at the same position, if so, udpate the table array
        superTarget = word + subTarget
        whatSuperTargetShouldBe = target[len(target)-len(superTarget):]
        if superTarget == whatSuperTargetShouldBe:
          table[len(superTarget)] = True
  
  return table[len(target)]

# Some test examples
assert can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == True
assert can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == True
assert can_construct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == False
assert can_construct("e" * 35 + "f", ["e" * i for i in range(1,8)]) == False