'''
Brick Wall (medium)

There is a rectangular brick wall in front of you with n rows of bricks. 
The ith row has some number of bricks each of the same height (i.e., one unit) 
but they can be of different widths. The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. 
If your line goes through the edge of a brick, then the brick is not considered 
as crossed. You cannot draw a line just along one of the two vertical edges of 
the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, 
return the minimum number of crossed bricks after drawing such a vertical line.

Example 1:


Input: wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
Output: 2

Constraints:
n == wall.length
1 <= n <= 104
1 <= wall[i].length <= 104
1 <= sum(wall[i].length) <= 2 * 104
sum(wall[i]) is the same for each row i.
1 <= wall[i][j] <= 231 - 1
'''

'''
Possible Solution: Length Minus Max Gaps
Time complexity: O(n)
Space complexity: O(n)

Set a hash table called gap and iterate through each row in the brick wall.
Set a variable called curr to go through the current amount of gaps the 
segment in the wall has. Set the value stored in the dictionary at curr to 1 + 
the current amount in the dictionary for each time it sees that gap. Finally, 
return the length of the wall minus the max value in the dictionary. This 
algorithm relies heavily on the len(wall) - max(gap.values()) and the counting 
of gaps it has encountered. This gets a somewhat similar idea to the mean value
of maximum amount of gaps which resolves itself to the minimum amount of bricks
to cross.

As the dictionary is needed for this solution and the iteration through the walls
does not repeat a value/the length of each row is bound by the length of wall,
the space and time complexity is O(n).
'''

def LengthMinusMaxGaps(wall):

    gap = {0:0}

    for w in wall:

        curr = 0

        for gaps in w:

            curr += gaps

            gap[curr] = 1 + gap.get(len(wall) - curr,0)

    return len(wall) - max(gap.values())


                

        
    




