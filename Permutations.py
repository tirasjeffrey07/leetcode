"""
leetcode 46

Given an array nums, return all the possible permutations

The order of the result doesnt matter

------------------------------------------------------------------------------------------------------------------
Recursion Approach:

- Divide each problem into multiple sub-problems
- we will use recursion to keep extending the subproblems
- The base is the empty list (return a list of a list if the length of array  = 0)
- at each permutation from the ground up (starting with a list of an empty list), insert the 0th element in all possible positions of the permutations

TC = O(n!) (n! x n², hence n!)

---------------------------------------------------------
Explanation
---------------------------------------------------------
Why 0th element?

consider [1,2,3] as the input

we wil recursivley call the function till we reach an empty array where [[]] will be returned

element to be inserted is 3 (from the subarray [3])
and theres only one position where 3 can be fit
=> [[3]]

element to be inserted is 2 (from the subarray [2,3])
we only take the 0th element coz we have already computed the permutations for [3]
there's 2 positions where 2 can be inserted and there's only one subarray where we need to insert:
=> [[2,3], [3,2]]

element to be inserted is 1 (from the subarray [1,2,3])
we take the 0th element as we have already computed permutations for [2,3]
there's 3 positions where 1 can be inserted, and there are 2 subarrays, so a total of 6 permutations can be obtained
for [2,3] => [1,2,3], [2,1,3], [2,3,1]
for [3,2] => [1,3,2], [3,1,2], [3,2,1]

so final result will be returned when we have reached the topmost subarray (which equals the actual array)

which is,
[[1,2,3], [2,1,3], [2,3,1], [1,3,2], [3,1,2], [3,2,1]]


------------------------------------------------------------------------------------------------------------------
Iterative approach:
- for every element 'n' in the array
- for every existing permutation 'p' in the list of permutations 'perms' (initially empty)
- add 'n' to every index 'i' in the the permutation 'p'

same time and space complexity as the recursive approach

---------------------------------------------------------
code:
---------------------------------------------------------
perms = [[]]

for n in nums:
    newPerms = []
    for p in perms:
        for i in range(len(p) + 1:) # element can be inserted in the last index as well
            pCopy = p.copy() # alter the copy not the actual array
            pCopy.insert(i, n)
            newPerms.append(pCopy)
    # update perms
    perms = newPerms
return perms


"""
from collections import List

def permute(self, nums: List[int]) -> List[List[int]]:
    # base case = return empty list
    if len(nums) == 0:
        return [[]]

    # each time, each sub-problem consists of the array devoid of the first element
    perms = self.permute(nums[1:])
    
    res = []
    
    # for each permutation
    for p in perms:
        # for each position in the permutation, including the last index + 1
        for i in range(len(p) + 1):
            pCopy = p.copy() # modify the copy not the original array
            # insert the 0th element in every position
            pCopy.insert(i, nums[0])
            # add the permutation to the result
            res.append(pCopy)
    
    return res

