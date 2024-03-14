"""
leet1582
Special Positions in a binary matrix

if a position[i][j] in a matrix is special it is said to obey the following conditions:
1) it is equal to 1
2) no other value in ith row and jth column should be 1

return the number of sepcial positions in the matrix


Note:
converting a list of lists into a single list with order retained can be done as follows:
a = [[1,0,0],[0,1,0],[0,0,1]]
print(sum(a,[]))
"""


"""
Brute force:

def numSpecial(self, mat: List[List[int]]) -> int:
    positions = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            rowMat = []
            if mat[i][j] == 1:
                if mat[i].count(1)==1 :
                    for k in range(len(mat)):
                        rowMat.append(mat[k][j])
                    if rowMat.count(1) == 1:
                        positions += 1
    return positions

"""

def specialSum(mat:list[list[int]]) -> int:
    positions = 0
    # to keep track of the number of 1s in each row
    rows = [0] * len(mat)
    # to keep track of the number of 1s in each column
    cols = [0] * len(mat[0])

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                #ith index of the row matrix will be incremented
                rows[i] += 1 
                #jth index of the column matrix will be incremented
                cols[j] += 1

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                # check only that rows and cols number of 1s
                if rows[i] == 1 and cols[j] == 1:
                    positions += 1
    return positions
    

print(specialSum(([1,0,0],[0,1,0],[0,0,1])))

