"""
213. House Robber II (medium)

You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. All houses at this place are 
arranged in a circle. That means the first house is the neighbor of the last 
one. Meanwhile, adjacent houses have a security system connected, and it 
will automatically contact the police if two adjacent houses were broken 
into on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the 
police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 \
(money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""


"""
Possible Solution: two variables

(Solution here can easily be cleaned up by using another function.) 

If length of nums is 1, return values at index 0. If not set up variables o 
and t. within range of the array until the second to last element, implement the house 
robber algorithm (see file houseRobber.py for explanation). set res to t and
do the same thing, except do not include the first value in the array. This is
done to make sure that the circular street does not have the two connected houses
that would cause the original algorithm to fail (can legally have the first and
last values be houses to rob in original, but in this case those would be next
to each other). Finally return the max of these two sub array processes.

As there is no data structure and uses two for loops that are independent of each
other, the runtime is O(n) and the space complexity is O(1).
"""

def TwoVariables(nums) -> int:
  
  if len(nums) == 1:
    
    return nums[0]
  
  o = 0
  
  t = 0
  
  for i in nums[:len(nums) - 1]:
    
    te = max(o + i, t)
    
    o = t
    
    t = te
    
  res = t
  
  o = 0
  
  t = 0
  
  for i in nums[1:]:
    
    te = max(i + o, t)
    
    o = t
    
    t = te
    
  return max(res, t)
  