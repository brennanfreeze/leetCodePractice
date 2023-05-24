'''
Two Sum (easy)

Given an array of integers nums and an integer target, return indices of the 
two numbers such that they add up to target. You may assume that each input 
would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''


'''
Possible Solution: Brute Force

Time Complexity: O(n^2)
Space Complexity: O(1)

Set a main for loop to iterate through the values in num. Set another for loop
to iterate all values in nums at index i + 1. If the values at these two
indexes summed up are equivalent to the target, return i and j.
'''

def BruteForce(nums, target: int):

    for i in range(len(nums)):

        for j in range(i + 1, len(nums)):
            
            if (nums[i] + nums[j] == target):

                return [i,j]
            
    return [-1, -1]



'''
Possible Solution: Hash Map

Time Complexity: O(n)
Space Complexity: O(n)

Set a hash map and proceed into a for loop in range of the length of nums.
If the target minus the value at index i is inside of the dictionary, this means
that this value has been seen before and we know that the value in the 
dictionary and the value at index i are the sums to target, so return i and the
index stored in the dictionary. If it is not equivalent, set the value at index
i as the key and i as the value in the dictionary to make sure the if statement
is valid in another step.
'''

def HashMap(nums, target: int):

    d = {}

    for i in range(len(nums)):

        if target - nums[i] in d:

            return [d[target - nums[i]], i]
        
        d[nums[i]] = i

    return [-1,-1]
