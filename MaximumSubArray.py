"""
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

----------------------------------------------------------------------
Use sliding window to get  O(n) time complexity

this is an inplace algo, so uses no extra space


Two pointers left and right are used
right keeps moving right,
we increment left if we encounter a negative value before a positive value

consider the above example,
-2 wont contribute to the sum it only decreases the value of 1 
so we discard it and move

simlarly we discard -3 coz it decreases the sum to 1 (-3+4)
"""

def maxSubArray( nums: list[int]) -> int:
    # 0th value by default to tackle 1 element arrays   
    maxSum = nums[0] 
    # used to keep track of the current sum
    currentSum = 0


    for number in nums:
        # avoidind negative values
        if currentSum < 0:
            currentSum = 0

        # then proceed to adding to the current sum value
        currentSum += number
        # finding the max between the current sum and the max val
        maxSum = max(currentSum,maxSum)

    return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

"""
Attempt 1 

prevSum,sum,i,j = 0,0,0,len(nums)

    while i<j:
        
        for pointer in range(i,j):
            sum += nums[pointer]
        
        if sum <= nums[0]:
            i += 1
            j -= 1
            prevSum = sum
            sum = 0
        
        else: break
    
    return sum

"""