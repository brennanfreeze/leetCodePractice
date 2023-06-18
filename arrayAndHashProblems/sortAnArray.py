'''
Sort An Array (medium)

Given an array of integers nums, sort the array in ascending order and return 
it.

You must solve the problem without using any built-in functions in O(nlog(n)) 
time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not 
changed (for example, 2 and 3), while the positions of other numbers are changed 
(for example, 1 and 5).

Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
'''


'''
Possible Solution: Binary Search Tree To Array
Time complexity: O(n^2)
Space complexity: O(n)

There are many ways to solve this problem, such as using heap sort, quick sort, 
and merge sort. This method implements a binary search tree first to sort through
the values. Within the question it is possible to have multiple of the same 
values, so to handle that the binary search tree sets the duplicate value to the
left branch of the node. After the binary search tree is set up, It uses a DFS
algorithm to append to an array each value it encounters from the left side
first, then the root node, then the right side of the tree. Finally, it returns
the array of values. 

As there is no added parameter to confirm that the binary search tree is 
balanced (ex: if 1-10000 was added in linear fashion and 10001 was needed to be
added, it would technically be a glorified array) the worst time case is going 
to be O(n) for inserting values. To get worst time complexity of log2n, a 
implementation of an AVL or a black and red algorithm would need to be done. 
Space complexity of the
'''

class Node:
    def __init__ (self, int_value):
        self.value = int_value
        self.left = None
        self.right = None

def insert(node: Node, int_value: int):

    if node is None:

        return Node(int_value)
    
    elif (node.value < int_value):

        node.right = insert(node.right, int_value)

    else:
        node.left = insert(node.left, int_value)

    return node

def InsertAndSort(arr):

    r = Node(arr[0])

    for i in range(1,len(arr)):

        r = insert(r, arr[i])

    res = []

    def sort(node):

        if node:

            sort(node.left)

            res.append(node.value)

            sort(node.right)

    sort(r)

    return res






