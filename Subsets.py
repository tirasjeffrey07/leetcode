"""
given nums return all the subsets of nums

ie 2 ^ n subsets

"""
from collections import List
def subsets(self, nums: List[int]) -> List[List[int]]:
    subsets = []
    res = []
    def backtrack(i):
        if i >= len(nums):
            res.append(subsets.copy())
            return 

        # add the element
        subsets.append(nums[i])
        backtrack(i + 1)

        # remove the element one by one
        subsets.pop()
        backtrack(i + 1)
    
    backtrack(0)
    return res
    


"""
nums = [1,2,3]

call 1:
dfs(0)
subsets = [1]

call 2:
dfs(1)
subsets = [1,2] 

call 3:
dfs(2)
subsets = [1,2, 3] 

call 4:
dfs(3)
i >= len(nums) so we add the subsets list to the result list res
function returns now

call 3 returns:
subsets.pop()
dfs(3) is called

call 5:
dfs(3)
3 >= len(nums)
[1,2] is appended to res


"""