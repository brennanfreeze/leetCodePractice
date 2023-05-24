'''
Selection Sort

Sorting algorithm for arrays.

Time Complextiy: O(n * n) = O(n^2)
Space Complexity: O(1)

Switch values based on the minimum value
min_val is first set to i, an indexthen, proceeds in the for 
loop of j which goes to i + 1 -> length of array.
If the value in j is less than the value in the index of min_val, then the 
min_val is set to j.  Finally, (not necessary but added to stop swap step,
which can be another possible unnecessary step) if min_val != arr[i],
then swap the value in index i and index min_val.

The first for loop goes through n steps, with that at worst case, 
the second for loop will go through n steps, making this process O(n^2).
'''

def SelectionSort(arr):
    for i in range(len(arr)):

        minimum_value = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[minimum_value]:

                minimum_value = j

        if arr[i] != arr[minimum_value]:

            arr[i], arr[minimum_value] = arr[minimum_value], arr[i]

    return arr