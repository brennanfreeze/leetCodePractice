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

Please check out the description in the dsaBasics directory for a detailed
explanation of how bubble sort is working. This is mainly to show that any
sorting algorithm technically can be done to solve this problem but they are
not efficient nor the right tool for a bounded amount of different values.
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

Set three variables as low, mid, and high where low and mid are set to 0 and 
high is set to the length of the nums. while mid <= high (used to determine when
the 1's and 2's sections meet) determine what the current middle value is equal
to. If it is equal to 0, switch the low index (0 section) with the middle and 
increment both low and mid (need to do this for low variable to keep the value
that was just sorted). If the value is equal to 2, do the same thing for 
the mid and high value and only set the high value to -1 of itself (the curr mid
value has not been determined if it is in the right spot so if one were to 
implement mid += 1 then there would be unsorted values). Finally, if it is equal
to one, just increment the mid value by one as it is in the current right spot.

As there is no need for extra space complexity and the entire algorithm is 
bounded by the length of nums, the time complexity is O(n) and the space 
complexity is O(1).
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
