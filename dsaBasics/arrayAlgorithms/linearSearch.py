'''
Linear Search

To find a value within an array

Time Complextiy: O(n)
Space Complexity: O(1)

A simple linear search algorithm that finds a given value to see if it is in the
array. If it is it will return true, if it is not there, then it will return 
false.

As this is only using one for loop to iterate through the entire array, the time 
complexity is going to be O(n).
'''

def LinearSearch(arr, value):

    for i in range(len(arr)):

        if (arr[i] == value):

            return True
        
    return False