'''
Concatenation of Array (easy)

Given an integer array nums of length n, you want to create an array ans of 
length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n 
(0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.

 

Example 1:

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
'''


'''
Possible Solution: Append values to end of new array
Time Complexity: O(n)
Space Complexity: O(n)

Set l to the current length of nums, while i is in range of l, append each 
value to the end of the array and return it. It is much easier to also just do
return nums + nums for the same idea. 

This is going to be a runtime of O(n * 2) for the size of the array and O(n * 2)
for the space compelxity of the algorithm
'''

def AppendToEnd(nums):
    l = len(nums)
    for i in range(l):
        nums.append(nums[i])
    # or just do return nums + nums instead of this
    return nums


'''


'''