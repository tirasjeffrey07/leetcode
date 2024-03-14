"""
def minFallingPathSum(matrix: list[list[int]]) -> int:
    paths = []
    pathSum = 0
    for i in range(3):
        pathSum += matrix[0][i]
        for j in range(3):
            pathSum += matrix[1][j]
            for k in range(3):
                pathSum += matrix[2][k]
                paths.append(pathSum)
                pathSum = matrix[0][i] + matrix[1][j]
    return min(paths)
"""


"""
This approach uses recursion and memoisation/ caching to keep track of already visited  paths

has a time complexity of n2 which can be reduved to o(n)
"""


def minFallingPathSum(matrix: list[list[int]]) -> int:
    N = len(matrix)

    # cache is used to store already computed locations
    cache = {}  # (r,c) is the key and its resultant is the value

    def dfs(r, c):
        # checking if we go out of bounds

        # if we've reached the last row
        if r == N:
            return 0

        # if we go beyond rightmost or leftmost columns
        if c < 0 or c == N:
            return float("inf")

        # we check if this position has already been visited
        if (r, c) in cache:
            return cache[(r, c)]  # itll return the result

        # else find min of (r+1,c), (r+1,c-1), (r+1,c+1)
        # matrix[r][c] is the current element
        res = matrix[r][c] + min(dfs(r + 1, c + 1), dfs(r + 1, c), dfs(r + 1, c - 1))
        cache[(r, c)] = res
        return res

    # starting from the worst, then we minimise it as much as we can
    res = float("inf")

    # iterating through every single column in the first row
    for c in range(N):
        res = min(dfs(0, c), res)

    return res


"""
direct DP solution using in place result storage
using bottom-up DP
"""


def minFallingPathSum(matrix: list[list[int]]) -> int:
    N = len(matrix)

    # float("inf") acts as the invalid marker

    # skipping the first row as it already has the values computed
    for r in range(1, N):
        # iterating through every single column
        for c in range(N):
            mid = matrix[r - 1][c]

            # assign only if its NOT the left most column
            left = matrix[r - 1][c - 1] if c > 0 else float("inf")

            # assign only if its NOT the rightmost element
            right = matrix[r - 1][c + 1] if c < N - 1 else float("inf")

            # updated value = current + min from row thats below
            matrix[r][c] = matrix[r][c] + min(left, right, mid)

    # return the min in the last row
    return min(matrix[-1])
