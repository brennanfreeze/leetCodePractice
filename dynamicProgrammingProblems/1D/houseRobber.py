"""
198. House Robber (medium)

You are a professional robber planning to rob houses along a street. Each house 
has a certain amount of money stashed, the only constraint stopping you from 
robbing each of them is that adjacent houses have security systems connected and 
it will automatically contact the police if two adjacent houses were broken into
on the same night.

Given an integer array nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the 
police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) 
and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


"""
Possible Solution: Use two variables

Set two variables o and t to 0. Within range of nums. Determine the max of the 
current count of o (in later increments, it is used to get the previous house)
plus the current value stored in i, or t (which is used as the current max 
account for later increments in the array). Set this to te, have o set itself
to t to keep track of the previous house, and finally set t to te, the current
max value that can be used in the max statement above in another iteration.
Finally, return t.

As this requires two variables and a single for loop bounded by n, the time 
complexity is going to be O(n) and the space complexity is going to be O(1).
"""

def TwoVariables(nums) -> int:
  o = 0
  t = 0
  for i in nums:
    te = max(i + o, t)
    o = t
    t = te
  return t