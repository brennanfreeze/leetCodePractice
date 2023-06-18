'''
Replace Elements with Greatest Element on Right Side (easy)

Given an array arr, replace every element in that array with the greatest 
element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.
'''

'''
Possible Solution: Brute Force
Time Complexity : O(n^2 / 2) = O(n^2)
Space complexity: O(1)

As simple of an algorithm as it can get for searching for values. Set a first
iteration in bounds of the input array. Set a second array in bounds of the 
index of i + 1 to the length of the array. set a current max within this range
and set the current i index to the max value. Do this for every value and return
the array.

The time complexity will be O(n^2 / 2) or O(n^2) in simplified terms and a space
complexity of O(1). 
'''

def BruteForce(arr):

    for i in range(len(arr)):

        currMax = -1

        for j in range(i + 1, len(arr)):

            currMax = max(currMax, arr[j])

        arr[i] = currMax

    return arr



'''
Possible Solution: Sort Sub Array
Time complexity: O(n^2 * logn)
Space complexity: O(n)

Please do not use this answer if stuck on finding a solution for this problem.
Within range of the array, sort the sub array of all values to the right of the 
current index and get the the last element in the array and set the current 
index to that value. Do so for every value and then set the last value in the
index to -1 and finally return the array.

As this needs to resort multiple values every iteration, the time complexity is
going to be O(n^2 * logn), the n^2 comes from the re sorting of values and the 
space complexity is going to be o(n) for using a sorting algorithm of nlogn.
'''

def SortSubArray(arr):

    for i in range(len(arr) - 1):

        sub_arr = sorted(arr[i + 1:])

        arr[i] = sub_arr[-1]

    arr[-1] = -1

    return arr


'''
Possible Solution: Iterate and keep track of max
Time complexity: O(n)
Space complexity: O(1)

Iterate backwards in range of the input array and set a max value as -1. Set a 
temp max variable called t_m to keep track of previous max value. On the current
index, determine if that value is greater than the current max value. Finally,
set the temp max value to the be at the index of i. 

As there is no need for extra space to determine the solution and it is bounded
in time by the length of the array alone, the time complexity is O(n) and the 
space complexity is O(1).
'''

def TrackMax(arr):

    m = -1

    for i in range(len(arr) - 1, -1, -1):

        t_m = m

        m = max(m, arr[i])

        arr[i] = t_m

    return arr



        
            


