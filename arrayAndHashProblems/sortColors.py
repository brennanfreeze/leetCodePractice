'''
Sort Colors (medium)

Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, with the 
colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, 
and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]

Constraints:

n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.
'''

'''
Possible Solution: Use n^2 Sorting Algorithm

Time Complexity: O(n^2)
Space Complexity: O(1)
'''

def BubbleSort(nums):
    
    for i in range(len(nums)):

        j = len(nums) - i - 1

        while j < len(nums) - 1 and nums[j] > nums[j + 1]:

            nums[j], nums[j + 1] = nums[j + 1], nums[j]

            j += 1

    return nums


'''
Possible Solution: Use Dutch Flag Algorithm

Time Complexity: O(n)
Space Complexity: O(1)

'''

def DutchFlag(nums):

    low = 0

    high = len(nums) - 1

    mid = 0

    while mid <= high:

        if nums[mid] == 0:

            nums[low], nums[mid] = nums[mid], nums[low]

            low += 1

            mid += 1

        elif nums[mid] == 2:

            nums[mid], nums[high] = nums[high], nums[mid]

            high -= 1

        else:

            mid += 1

    return nums
