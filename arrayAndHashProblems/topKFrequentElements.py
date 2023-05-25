'''
Top K Frequent Elements (medium)

Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
'''


'''
Possible Solution: Brute Force

Time Complexity: O(n^2 + (k * n))
Space Complexity: O(n)

Create a dictionary to hold the value and the count of the value in nums.
Within a for for loop, count the number of times you encounter this value and
set it to the dictionary. Next, set an empty array called res and get the max
value in the dictionary values and its corresponding key value. Finally 
append the key to the res array k times for the most frequent elements and then
pop the key to get the next max value.

The first for loop will generate a O(n^2) runtime and the next for loop with 
k and the search through the dictionary in linear time to find the key will be 
O(k * n). combined this will be: O(n^2 + (k * n)). Space complexity will come
from the hash table being used so it will be O(n).
'''

def BruteForce(nums, k):

    d = {}

    for i in range(len(nums)):

        count = 0

        for j in range(len(nums)):

            if (nums[j] == nums[i]):

                count += 1

        d[nums[i]] = count

    res = []

    for i in range(k):

        m = max(d.values())

        max_key = [key for key, value in d.items() if value == m]

        res.append(max_key[0])

        d.pop(max_key[0])

    return res


'''
Possible Solution: 2D Array and Hashmap (bucket sort)

Time complexity: O(n)
Space complexity: O(n)

Create a dictionary and a 2d array which is the length of the input nums + 1.
Set the count of each unique value from nums into the dictionary. Then using the
count of those values as indexes in t, the 2d array, append the value for those
counts into the array at the index. This will sort the values by their occurance
together. Within another for loop, reverse iterate through the 2d array t within
range of the first index. For each array found at the index of each iteration of
t, append the value to res until the length of res is the same as the value for
k, in which return res.

The one nested array and it is going through all the values that
are possible only once, this is still O(n) and the other for loops equate to the
same using big O abstraction of runtime. The space complexity using a hash map
is O(n) as well.
'''


def HashMap2D(nums, k):

    d = {}

    t = [[] for _ in range(len(nums) + 1)]

    for n in nums:

        d[n] = 1 + d.get(n, 0)

    for i, c in d.items():

        t[c].append(i)

    res = []

    for i in range(len(t) - 1, 0, -1):

        for n in t[i]:

            res.append(n)

            if (len(res) == k):

                return res
