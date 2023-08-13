'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown 
pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], 
nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become 
[4,5,6,7,0,1,2].

Given the array nums after the possible rotation8 and an integer target, return 
the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
'''

'''
Possible Solution: Binary Search
Time complexity: O(log2n)
Space complexity: O(1)

Create two pointers, l and r to represent the start and ending of the nums 
array. While l is less than or equal to r pointer, set a variable m to the 
halfway point between those two pointers. If the value at index m is the 
target, return the index of m. If not, two determinants come into play to 
find how the array is rotated. If the value at index m is greater than or equal
to the value at index l, then we know that the array is sorted on the left side,
but this could also mean than [1,2,3,0] where m is at 2 and left is at 1, so 
another inner understanding of where the value is at is needed. if value at m is 
less than target or target is less than value at index l, then we know that 
l pointer must be shifted up as the target is not in the left region of the 
array. Else, we know the value is in the left region so shift the r pointer to
the left side. The next determinant is if the value at m is less than the value
at l. Then we know that the array has been rotated and the larger values are 
most likely on the left side. From here we determine if the value at m is less
than the target or the target is greater than the right pointer. This is to 
validate that the target value no matter the sequence the l and r pointers are
in, the value is on the left side of the array, so set r to m - 1. If these two
conditions are not met, set the l pointer to the right side of the search region
as we know it cannot be on the left side of the search region. Do this until 
either the target value is found, or if it does not exist, return -1 as it is
not in the array

As this algorithm divides the search region in the array for the target value
by two on each step, we can determine that this algorithm runs in log2n and the
space complexity is O(1).
'''

def BinarySearch(nums, target: int):
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if (nums[m] == target):
            return m
        if (nums[m] >= nums[l]):
            if (nums[m] < target or target < nums[l]):
                l = m + 1
            else:
                r = m - 1
        else:
            if (target < nums[m] or target > nums[r]):
                r = m - 1
            else:
                l = m + 1
    return -1
