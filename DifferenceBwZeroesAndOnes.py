"""
leet2482

You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.

diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj

Return the difference matrix diff.

Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]
"""


def onesMinusZeros(grid: list[list[int]]) -> list[list[int]]:
    r = len(grid)
    c = len(grid[0])

    # since were subtracting the number of zeroes from the number of ones
    onesRow = [0] * r
    zeroesRow = [0] * r
    onesCols = [0] * c
    zeroesCols = [0] * c

    diff =[ [ 0 ] * c ] * r
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 0:
                zeroesCols[j] += 1
                zeroesRow[i] += 1
            else:
                onesRow[i] += 1
                onesCols[j] += 1
    # print(onesCols, onesRow, zeroesCols,zeroesRow)
    matrix=[]
    row = []
    for i in range(r):
        for j in range(c):
            row.append(onesCols[j] + onesRow[i] - zeroesCols[j] - zeroesRow[i]) 
            # when weve come to last element in the row add row to matrix
            if j == c - 1:
                matrix.append(row)
                row = []
    return matrix


print(onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]]))

grid = [[0,1,1],[1,0,1],[0,0,1]]


