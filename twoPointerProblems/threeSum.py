'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


'''
Possible solution: Brute force
Time complexity: O(n^3)
Space complexity: O(1)

Go through every possible solution to determine if the for loop indices of 
i, j, and k are summed up to 0. If so append it to res and finally return res.

As there is three for loops going through multiple iterations, the time 
complexity is O(n^3) and the space complexity is O(1).  
'''


def BruteForce(nums):

    res = []

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):

            for k in range(j + 1, len(nums)):

                if nums[i] + nums[j] + nums[k] == 0:

                    res.append([nums[i], nums[j], nums[k]])

    return res


'''
Possible solution: Sort array and then go through sub sections
Time complexity: O(n^2)
Space complexity: O(n)

Sort the inputted array and set a res array to hold the combinations.
Within range of the sorted array, if the index at i is greater than 0, than we
know that there is no other solutions on the right side of that value and we 
can break from the for loop. If the index i is equal to the value at i - 1, then
we can continue on as we have already gone through those possible solutions.
Set two variables, l to i + 1, and r to the end of the array. Determine if those
indexes are equal to 0, if less than it increment l by one, if greater than, set
the r to r - 1. If it is actually equal to 0, do l += 1 and r -= 1 and then
set a while loop to iterate through duplicate values in the l region to 
minimize repitition of values. 
'''

def SortArray(nums):

    res = []

    nums.sort()

    for i in range(len(nums)):

        if nums[i] > 0:

            break

        if i > 0 and nums[i] == nums[i - 1]:

            continue

        l = i + 1

        r = len(nums) - 1

        while l < r:

            s = nums[i] + nums[l] + nums[r]

            if (s < 0):

                l += 1

            elif (s > 0):

                r -= 1

            else:

                res.append([nums[i], nums[l], nums[r]])

                l += 1

                r -= 1

                while l < r and nums[l] == nums[l - 1]:

                    l += 1

    return res