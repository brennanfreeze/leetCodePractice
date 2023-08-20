"""
152. Maximum Product Sub-array (medium)
Given an integer array nums, find a 
sub-array
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a sub-array.
 

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit 
integer.

"""

"""
Possible Solution: Brute Force (Needs Improvement for all cases)

""" 

def BruteForce(nums) -> int:
  
  res = nums[0]
  
  for i in range(len(nums)):
    
    t = nums[i]
    
    for j in range(i + 1, len(nums)):
      
      t = t * nums[j]
      
  for i in range(len(nums) -1, -1, -1):
    
    t = nums[i]
    
    for j in range(i - 1, -1, -1):
      
      t = t * nums[j]
      
    res = max(res, t)
    
  return res

"""
Possible Solution: Dynamic Programming (House Robber/Fibonacci Sequence)
"""

def DynamicProgramming(nums) -> int:
  
  res = nums[0]
  
  o = 1
  
  t = 1
  
  for n in nums:
    
    to = o * n
    
    ti = t * n
    
    o = max(to, ti, n)
    
    t = min(to, ti, n)
    
    res = max(res, o)
    
  return res