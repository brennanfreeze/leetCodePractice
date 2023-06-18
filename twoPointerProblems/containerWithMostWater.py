'''
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
'''

'''
Possible Solution: Brute Force
Time complexity: O(n^2)
Space complexity: O(1)

Create a variable to get the max area of a container and set a for loop to be
in bound of the length of height. Set a inner for loop in range of i + 1 and the
length of height. Determine the max value between the current max and the 
calculation of the min height of the values inside of i and j and the length of
j and i (basic area of a rectangle equation). Finally, return the max.

As this is using two for loop repeating steps on the same indices multiple times
the time complexity is O(n^2 / 2) = O(n^2) and the space complexity is O(1).
'''
def BruteForce(height):

    ma = 0

    for i in range(len(height)):

        for j in range(i + 1, len(height)):

            ma = max(ma, min(height[i], height[j]) * (j - i))

    return ma


'''
Possible solution: Two Pointers with Same Logic
Time complexity: O(n)
Space complexity: O(1)

Set three variables, ma being the return value, l being the left pointer, and 
r being at the end of the height array. While l is less than right, find the 
rectangle area in the same fashion as the above solution, however use an if
statement to determine if l or r is the smaller value and shift the two
pointers closer to each other depending on the size. Finally return ma.

As there is no need to revaluate values in indicies and uses no extra space 
complexity, the complexity is respectively O(n) and O(1).
'''

def TwoPointers(height):

    ma = 0

    l = 0

    r = len(height) - 1

    while l < r:

        t = min(height[l], height[r]) * (r - l)

        ma = max(ma, t)

        if (height[l] < height[r]):

            l += 1

        else:

            r -= 1

    return ma
        