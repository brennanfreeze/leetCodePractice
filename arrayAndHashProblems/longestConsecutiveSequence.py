'''
Longest Consecutive Sequence (medium)

Given an unsorted array of integers nums, return the length of the longest 
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. 
Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
'''

'''
Possible Solution: Brute Force

Time Complexity: O(n^2)
Space Complexity: O(n)

If the length of nums is 0, return 0. Get all unique values in the nums array
sorted. set the first value in the index as the min_val and set a return value
res as 1. Setting nums as a queue, set three variables. nums_temp = nums to
iterate through the current queue, was_increment to see if there was an 
increment value, and temp_res to see if the current res needs to be replaced.
within the range of nums_temp, see if the current front of queue is equal to
min_val + 1. If it is, was_increment = true, temp_res += 1 and min_val is equal
to that value and pop it from the queue. If not, append the value to the end of
the queue. After the for loop, if there was no increment, set the min_val to
the current front of queue and pop that from temp_nums. res is then determined
if that current iteration of the increments was bigger than the last using max
and nums is set to temp_nums.

This is a highly inefficent algorithm similar to BFS layout, only this situation
the need to insert it back into the queue is necessary so a lot of efficiency is
lost. The inner for loop then will brute force the entire array looking for a 
value. Although the time compelxity is technically O(nlogn + n^2), the n^2 takes
over so the time complexity is (n^2) and the space complexity is O(n).
'''

def BruteForce(nums):

    if len(nums) == 0:

        return 0
        
    nums = sorted(list(set(nums))) #nlogn
    
    min_val = nums.pop(0)

    res = 1

    while nums: # n

        nums_temp = nums

        was_increment = False

        temp_res = 1

        for _ in range(len(nums_temp)):
            
            if (nums_temp[0] == min_val + 1):

                was_increment = True

                temp_res += 1

                min_val = nums_temp.pop(0)

            else:

                nums_temp.append(nums_temp.pop(0))
            

        if not was_increment:

            min_val = nums_temp.pop(0)

        res = max(res, temp_res)

        nums =  nums_temp

    return res


'''
Possible Solution: Sorted Array

Time Complexity: O(nlogn)
Space Complexity: O(n)

Sort the array using sorted(). set three variables i, m and t_m to one to start
the process at index one and knowing that the first value in the array is the
start of a sequence. while i < length of nums, use two if statements to see
what is apart of the sequence, what is the same as the current iteration, and
when the sequence ends. We can tell if the sequence ends if the current index
is not equal to the curr and not equal to curr + 1. In this case reset t_m.
Use the second if statement to see if nums at i is not equal to curr, if not 
increment t_m. Set curr to the current index at i and determine the max 
between m and t_m.

As we need to sort the array before the implementation of the algorithm, the 
time complexity is going to be O(nlogn) and the space complexity is going to be
O(n) assuming the sorted() is implmenting quick sort with a random pivot.
'''


def SortedArray(nums):

    if (len(nums) == 0):

        return 0
    
    nums = sorted(nums)

    i = 1

    m = 1

    t_m = 1

    curr = nums[0]

    while i < len(nums):

        if (nums[i] != curr + 1 and nums[i] != curr):
            t_m = 0
        
        if (nums[i] != curr):
            t_m += 1

        curr = nums[i]

        m = max(t_m, m)

        i += 1

    return m


'''
Possible Solution: Set
Time Complexity: O(n)
Space Complexity: O(n)

Set nums to be a set. have variables res and t_res to validate the amount of 
iterations. Iterating through the values in num, determine if n - 1 is in the
set or not. This will determine if a sequence is beginning or not in the set.
If it is the start of a sequence, start a while loop determining if there is an
iteration found through the set. If there is, t_res += 1 and t += 1. After
the while loop, set res to the max of t_res and res.

Although there is an inner for loop, the for loop still iterates through the 
main array and all elements are stepped through only once using the t += 1
in it. This means that the time complexity is O(n) and the space complexity is
O(n) as well for the set.
'''

def Set(nums):

    if len(nums) == 0:

        return 0
    
    nums = set(nums)

    res = 1

    t_res = 1

    for n in nums:

        if (n - 1 not in nums):

            t_res = 1

            t = n

            while t + 1 in nums:

                t_res += 1

                t += 1

            res = max(t_res, res)
        
    return res