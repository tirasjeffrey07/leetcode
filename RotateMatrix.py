"""
Leetcode-48

Rotate matrix in-place, DO NOT USE ANOTHER 2D MATRIX

dont return anything


i suggest watching neetcode's video on this, 
he explained it in a very clear way

"""

def rotate(self, matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    # n x n matrix
    left, right = 0, len(matrix) - 1

    # at each iteration we:
    # increment l, decrement r
    # increment top, decrement bottom
    while left < right:
        # perform the shifting of element n - 1 times 
        # ie if there are 4 elements, you shift positions only 3 times 
        for i in range(right - left):
            # at each iteration, we shift to the adjacent index to rotate the next square\
            # this is done by adding the i to the indices to alter them
            top, bottom = left, right

            # save top left coz that's going to be overwritten first
            topLeft = matrix[top][left + i]

            # bottom left element -> top left 
            matrix[top][left + i] = matrix[bottom - i][left]
            
            # bottom right element -> bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # top right element -> bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            
            # top left element -> top right
            matrix[top + i][right] = topLeft
        # go for inner square
        left += 1
        right -= 1