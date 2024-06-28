"""
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums except nums[i].

The code should run in O(N) and shouldnt use division operator

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""





# final solution - O(n)
# take 1,2,3,4
def productExceptSelf(nums:list[int]) -> list[int]:
    answer = [1] * len(nums)
    prefix,postfix = 1,1

    # calculating the prefix array first,
    # prefix = 1,1,2,6
    for i in range(len(nums)):
        answer[i] = prefix
        prefix *= nums[i]

    
    # multiplying the postfix with the array that 
    # already contains the prefix values, 
    # hence eliminating the need for an extra array 
    # postfix = 
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]

    return answer

print(productExceptSelf([1,2,3,4]))