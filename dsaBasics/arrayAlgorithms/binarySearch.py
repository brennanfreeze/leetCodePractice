'''
Binary Search

Efficient manner to search through a sorted array

Time complexity: O(log2n)
Space complexity: O(1)

Start with two pointers, one at index 0 of the array, and at the index of the
length of the array -1. A while loop determines if the left variable (index 0)
is less than or equal to the right variable (index length of array -1). This is
to stop the loop as if the left pointer is greater than the right pointer, then
we know that the value does no exist in the space of the array. The = in the <=
is to ensure that value is still spotted. Within the for loop, set a variable
called middle, which is the index of (l + r) // 2 to find the halfway point of 
the two indexes. If the middle value is equal to the desired value, then return
true. Else, determine the size of the value in the index middle to the desired
value. If the desired value is greater than the middle index value, then we know
to search the right side of the array so set the left pointer to middle + 1. 
Else, we know the desired value is less than the middle index value so set the
right pointer to middle - 1.

As you are dividing the array search area into two on each step, 
it can be concluded that: ((n / 2) / 2...) / 2 is equivalent to the time 
complexity of O(log2n).
'''

def BinarySearch(arr, value):

    left = 0

    right = len(arr) -1

    while (left <= right):

        middle = (left + right) // 2

        if (arr[middle] == value):

            return True
        
        elif (arr[middle] < value):

            left = middle + 1

        else:

            right = middle - 1

    return False