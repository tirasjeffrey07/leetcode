"""

leetcode 807

There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.

A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.

We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.

Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction

------------------------------------------------------------------------------------
Example 1:

Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35

Explanation: The building heights are shown in the center of the above image.
The skylines when viewed from each cardinal direction are drawn in red.
The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

------------------------------------------------------------------------------------
Example 2:

Input: grid = [[0,0,0],[0,0,0],[0,0,0]]
Output: 0
Explanation: Increasing the height of any building will result in the skyline changing.
------------------------------------------------------------------------------------
Explanation:

- Each element represents a building in the spot with height
- We look at the city from north, south, east and west
- the skyline is made up of the highest building in each row (when looking from south or north) and the highest in each column (when looking from east or west)
- Consider example 1,
    say you're standing in the north, looking towards south (NS direction)
    the skyline would be [9, 4, 8, 7]
    we can increase all elements of col 1 till it reaches 9, elements of col2 till it reaches 4, elements of col3 till it reaches 8 and col4 elements till it reaches 7

    Similarly we do this for all 4 directions, and return the amount of height values we've increased


Approach:
- Calculate the max height of every row and column
- for building[i][j], min(maxOfRow[i], maxOfColumn[j]) is the threshold, which means that this is the max amount to which we can increase the height so it doesnt affect the skyline (max height of that build in row and column)
- find the difference of the current height of the building and the threshold, add it to a result sum
- return result sum
"""



from typing import List

def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
    res = 0
    n = len(grid)
    # initialising arrays of size n
    maxRowVals, maxColVals = [0] * n ,[0] * n

    for i in range(n):
        for j in range(n):
            maxRowVals[i] = max(maxRowVals[i], grid[i][j])
            maxColVals[j] = max(maxColVals[j], grid[i][j])
    
    
    for i in range(n):
        for j in range(n):
            res += min(maxRowVals[i], maxColVals[j]) - grid[i][j]

    return res