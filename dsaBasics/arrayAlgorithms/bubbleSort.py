'''
Bubble Sort

Algorithm to sort an array within a O(1) space complexity.

Time Complexity: O(n^2)
Space Complexity: O(1)

The first for loop sets itself to be in range of the array's length. The second
for loop sets itself to be in range of 0 -> length of array - i  - 1 to start at
the unsorted section of the array. The if statement within the j based for loop
will determine if the value at index j + 1 < value at j. if so, then switch 
the two values. The main purpose of the of bubble sort is to shift elements that
are bigger first, and assumes that the smaller values will follow suit.

The main for loop goes through the array's length, and the second for loop at 
worst can go from index 0, to the length of the array. With this, we can 
determine that the time complexity is going to be O(n * n) or O(n^2).
'''


def BubbleSort(arr):

    for i in range(len(arr)):

        for j in range(0, len(arr) - i - 1):

            if (arr[j] > arr[j + 1]):

                arr[j + 1], arr[j] = arr[j], arr[j + 1]

    return arr


