'''
Product of Array Except Self (medium)

Given an integer array nums, return an array answer such that answer[i] 
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to 
fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and 
without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

'''
Possible Solution: Forwards and Backwards using three arrays

Time Complexity: O(n)
Space Complexity: O(n)

Create a prefix array which sets itself to an array of zeros with the length the
same as the length of nums. Set the first index value in nums as the first value
in prefix. For in range of index one to the end of nums, set each index of prefix
to be prefix[i - 1] * nums[i] to get all the values multiplied at the current
index with the one previously in prefix. Do this but in complete opposite reverse
style for a postfix array. finally, create an output array that determines if the
we are at the index 0 or last index in the nums array using left and right to 
make sure we do not try and multiply a value out of range. if they are not, set
the respective left and right pointers to the prefix and postfix array values
that were calculated in previous steps. Set index in output of the left and right
values multiplied and then return output.

Using no inner dependent for loops, we get a runtime complexity of O(n * 3),
which is converted to just O(n) for runtime compelxity. For space complexity, it
is the same process and it is O(n).
'''

def ThreeArrays(nums):

    prefix = [0] * len(nums)

    prefix[0] = nums[0]

    for i in range(1, len(nums)):

        prefix[i] = prefix[i - 1] * nums[i]

    postfix = [0] * len(nums)

    postfix[-1] = nums[-1]

    for i in range(len(nums) - 2, -1 ,-1):

        postfix[i] = postfix[i + 1] * nums[i]
    
    output = [0] * len(nums)

    for i in range(len(nums)):

        left = 1

        right = 1

        if (i > 0):

            left = prefix[i - 1]

        if (i < len(nums) - 1):

            right = postfix[i + 1]

        output[i] = left * right

    return output


'''
Possible Solution: Combine Into One Array
Time Compelxity: O(n)
Space Complexity: O(1) (output array is O(1) according to problem)

Not a trivial connection to above, but follow the same idea of using prefix
and postfix calculations. Take a output array and set it to be an array of 1's 
to the length of the nums array. within range of nums, set output index to 
prefix, then set prefix to be nums[i] * prefix to build up the values of previous
multiplication calculations. Do another for loop for postfix calculations except
multiply the postfix value with the current output index and then do the same
process as the prefix for loop.

As the output array is considered O(1) in this problem and uses no inner 
dependent for loops, the runtime complexity is: O(n) and the space complexity is
O(1).
'''

def OneArray(nums):

    output = [1] * len(nums)

    prefix = 1

    for i in range(len(nums)):

        output[i] = prefix

        prefix = nums[i] * prefix

    postfix = 1

    for i in range(len(nums) -1, -1, -1):
        
        output[i] *= postfix

        postfix *= nums[i]

    return output


