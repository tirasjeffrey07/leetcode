
"""

leetcode 1863

given an array nums return the sum of all the XOR totals of every sub array


"""


from collections import List

def subsetXORSum(self, nums: List[int]) -> int:
    res = 0 

    def dfs(i, total):
        if i >= len(nums):
            return total
    
        
        return dfs(i + 1, total ^ nums[i]) + dfs( i + 1, total)
    
    return dfs(0, 0)
