
from math import prod
def product_except_self(nums):
  '''
  Given an integer array nums, return an array answer such that 
  answer[i] is equal to the product of all the elements of nums 
  except nums[i].

  The product of any prefix or suffix of nums is guaranteed to fit
  in a 32-bit integer.

  https://leetcode.com/problems/product-of-array-except-self/
  '''

  # Key insight is that the number of times that zero appears is critical!
  zero_count = nums.count(0)

  # * If zero appears twice or more, the entire result is globally zero
  #   since there is no position that we can remove zero as a factor
  if zero_count >= 2 or zero_count == len(nums):
    return [0] * len(nums)
  
  # * If zero appears  only once, then every position except the one for
  #   zero will be zero
  elif zero_count == 1:
    # Need the product without zero, which will be the value everywhere
    # except the position where zero appears
    product = prod(filter(abs, nums))
    return [0 if num != 0 else product for num in nums]
  
  # * If zero doesn't appear at all, we can simply divide the total product
  #   by the value at each position
  product = prod(nums)
  return [product // num for num in nums]

assert product_except_self([0,4,0]) == [0,0,0]
assert product_except_self([1,0]) == [0,1]
assert product_except_self([1,2,3,4]) == [24,12,8,6]
assert product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]
