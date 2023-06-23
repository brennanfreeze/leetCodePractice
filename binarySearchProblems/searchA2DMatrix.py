'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous 
row. Given an integer target, return true if target is in matrix or false 
otherwise.

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
'''

'''
Possible Solution: Binary Search
Time complexity: O(m * logn)
Space complexity: O(1)


'''

def LinearAndBinarySearch(matrix, target: int) -> bool:

    for row in range(len(matrix)):

        l = 0

        r = len(matrix[row]) - 1

        while l <= r:

            m = (l + r) // 2

            if matrix[row][m] == target:

                return True
            
            elif matrix[row][m] < target:

                l = m + 1

            else:

                r = m - 1

    return False

'''
Possible Solution Pure Binary Search
'''
def PureBinarySearch(matrix, target: int) -> bool:
    
    rows = len(matrix)

    cols = len(matrix[0])
    
    left = 0

    right = rows - 1

    while left <= right:

        middle = (left + right) // 2

        if (target == matrix[middle][-1] or target == matrix[middle][0]):

            return True
        
        if (target > matrix[middle][-1]):

            left = middle + 1

        elif(target < matrix[middle][0]):

            right = middle - 1

        else:

            break
            
    if not (left <= right):

        return False
    
    row = (left + right) // 2

    l = 0

    r = cols - 1

    while l <= r:

        middle = (l + r) // 2

        if (matrix[row][middle] < target):

            l = middle + 1

        elif(matrix[row][middle] > target):

            r = middle - 1
            
        else:
            return True
        
    return False
   