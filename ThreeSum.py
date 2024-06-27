"""
leet 15 

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 
-----------------------------------------------------------------------------------------

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.

The distinct triplets are [-1,0,1] and [-1,-1,2].

-----------------------------------------------------------------------------------------
Notice that the order of the output and the order of the triplets does not matter.

Naive: O(N³)
-----------------
calculate every triplet, find sum that = 0

Optimal: O(N²)
-----------------
first sort the array so the smallest are towards the left and the largest are towards the right
For each index i,
l = i + 1, r = last index
if the sum of arr[l] + arr[r] + arr[i] == 0:
    append it to the list
elseif the sum is greater than 0:
    decrement right pointer (to use numbers with lesser values)
elseif the sum is lesser than 0:
    increment left (to use numbers with greater values)

now, we increment left even if we find the sum coz there is more than one triplets which sum to 0

we may even have duplicates from the left
so we have to check that as well
while nums[l] == nums[l-1]:
    l+=1

"""



from collections import List

def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    res = []
    for i, val in enumerate(nums):
        if i > 0 and val == nums[i-1]:
            continue # skip duplciates in the array eg : [-3,-3,-2,-1,1,2,2,3]
        j, k = i+1, len(nums) - 1
        while j < k:
            sm = val + nums[j] + nums[k] 
            if sm == 0:
                res.append([val, nums[j], nums[k]])
                j += 1
                # the below loop is to avoid the following error
                # -2 -2 0 0 2 2
                #  l          r
                #     l
                # in both cases sum = 0 so we do that avoid repeating left values
                while nums[j] == nums[j-1] and j < k:
                    j += 1
            elif sm > 0:
                k -= 1
            elif sm < 0:
                j += 1
    return res