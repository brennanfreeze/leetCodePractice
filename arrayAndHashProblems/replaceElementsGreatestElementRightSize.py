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

'''

def SortSubArray(arr):

    for i in range(len(arr) - 1):

        sub_arr = sorted(arr[i + 1:])

        arr[i] = sub_arr[-1]

    arr[-1] = -1

    return arr


'''
Possible Solution: Iterate and keep track of max

'''

def TrackMax(arr):

    m = -1

    for i in range(len(arr) - 1, -1, -1):

        t_m = m

        m = max(m, arr[i])

        arr[i] = t_m

    return arr



        
            


