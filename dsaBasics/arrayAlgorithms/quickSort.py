'''
Quick Sort With Random Pivot
'''

import random

def partition(arr, low, high):

    pivot = arr[low]

    i = low + 1

    j = high

    while True:

        while i <= j and arr[i] <= pivot:

            i += 1

        while i <= j and arr[j] >= pivot:

            j -= 1

        if i <= j:

            arr[i], arr[j] = arr[j], arr[i]

        else:

            break

    arr[low], arr[j] = arr[j], arr[low]
    
    return j

def partition_random(arr, low, high):

    r = random.randrange(low, high)

    arr[r], arr[low] = arr[low], arr[r]

    return partition(arr, low, high)

def QuickSort(arr, low, high):

    if low < high:
        
        p = partition_random(arr, low, high)

        QuickSort(arr, low, p - 1)

        QuickSort(arr, p + 1, high)


arr = [1,2,5,221,6,3,7,4,3,6,3,6,3,2345,67,2,23,4,6,7,3,3,1,45,4]
QuickSort(arr, 0, len(arr) - 1)
print(arr)