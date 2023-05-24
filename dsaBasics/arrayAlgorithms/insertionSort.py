'''
Insertion sort

Sorting algorithm for arrays

Time Complexity: O(n * n) = O(n^2)
Space Complexity: O(1)

start with a for loop that is in range of the length of array. Set a key value 
to the current value in index i and a value j as i - 1. Set a while loop that
has j go backwards in the array starting from i - 1 and will stop at when
j >= 0 and if key > arr[j], meaning that if at index j we have 5 and the key
is 7, then it is known that the swapping values must stop as that is in a sorted
area of the array. If the statements are false, then swap the value in index
j + 1 with j until this break point occurs.

The main for loop has n steps (length of the array) and the while loop at worst
can do n steps (having let's say 1 being the smallest value be at the far 
right of the array,then we must have the 1 go all the way the left side). This
means that the time complexity is O(n * n) or O(n^2).
'''

def InsertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:

            arr[j + 1], arr[j] = arr[j], arr[j + 1]

            j -= 1

    return arr

