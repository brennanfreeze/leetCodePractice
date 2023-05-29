'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily 
solvable.
Only the filled cells need to be validated according to the mentioned rules.
Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
'''


'''
Possible Solution: Brute Force

(Technically is always O(1) but in my opinion, this problem should handle n * n
grids instead of constant 9 * 9 as it would solidify perfect squares ideas.)
Time Complexity: O(n)
Space Complexity: O(n)

Split problem into each requirement from the sudoku board.
Each one of the steps uses a set to make sure each value is
unique. (1) Validate each and every column to make sure that they do not have 
repeating values in the columns. (2) Validate each row by making sure that there
is no repeated values in them. For each grid, set i and j to be the top left of
each grid. Set an inner for-for loop to iterate through each value in the grid
and determine if each square is valid. If all are valid return true

Although the values are evaluated multiple times in different sections, each for
loop section handling each case they do not iterate throuhgh multiple of the 
same values. This means that the space/time complexity in hindsight is both O(n)
'''
from math import sqrt

def BruteForce(board):

    in_each_grid = sqrt(len(board))

    for j in range(len(board[0])):

        col_set = set()

        for i in range(len(board)):

            if (board[i][j] in col_set):

                return False
            
            if (board[i][j] != '.'):

                col_set.add(board[i][j])

    for i in range(len(board)):

        row_set = set()

        for j in range(len(board[0])):

            if (board[i][j] in row_set):

                return False
            
            if (board[i][j] != '.'):

                row_set.add(board[i][j])

    i = 0

    while i < len(board):

        j = 0

        while j < len(board[0]):

            grid_set = set()

            for k in range(i, i + in_each_grid):

                for l in range(j, j + in_each_grid):

                    if (board[k][l] in grid_set):

                        return False
                    
                    if (board[k][l] != '.'):

                        grid_set.add(board[k][l])

            j += 3

        i += 3

    return True


'''
Possible Solution: Combine Each Step Into One

(Technically is always O(1) but in my opinion, this problem should handle n * n
grids instead of constant 9 * 9 as it would solidify perfect squares ideas.)

Time Complexity: O(n)
Space Complexity: O(n)

Using three default dictionary data structures whose values are set to sets, the
algorithm combines the three rules of a valid sudoku into one for-for loop. 
Within each cell of the board, determine if the set in the dictionary based on
the row, column, and grid (pair of i, j int divided by the perfect square 
length). Determine if that cell's value has been seen in a prior value in the 
sets. 

As each cell is only visited once, this means that the runtime despite having a
for-for loop is going to be O(n) and the usage of the hashmap sets is going to
be O(n) as well.
'''

from collections import defaultdict

def CombineSteps(board):
    
    in_each_grid = sqrt(len(board))

    row_set = defaultdict(set)

    col_set = defaultdict(set)

    grid_set = defaultdict(set)

    for i in range(len(board)):

        for j in range(len(board[0])):
            
            if (board[i][j] != '.' and 
                (board[i][j] in row_set[i] or
                board[i][j] in col_set[j] or 
                board[i][j] in grid_set[(i // in_each_grid, 
                                         j // in_each_grid)])):

                return False
            
            row_set[i].add(board[i][j])

            col_set[j].add(board[i][j])

            grid_set[(i // in_each_grid, j // in_each_grid)].add(board[i][j])

    return True



