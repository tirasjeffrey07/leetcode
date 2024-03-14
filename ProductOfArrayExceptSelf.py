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


""" 
Attempt 1

class Solution:
    def productExceptSelf(self,nums: list[int]) -> list[int]:
        #print("nums = ",nums)
        leftArray = left(nums)
        #print("left array = ",leftArray)
        rightArray = right(nums)
        #print("right array = ",rightArray)
        answer = []
        lengthOfArray = len(nums)
        if lengthOfArray == 0:
            return nums
        for i in range(lengthOfArray):
            if i == 0:
                answer.append(rightArray[lengthOfArray-2])
            elif i == lengthOfArray-1:
                answer.append(leftArray[lengthOfArray - 2])
            else:
                answer.append(leftArray[i-1]*(rightArray[::-1][i+1]))
        return answer

def left(numbers:list[int]) -> list[int]:
    answer = []
    product = 1
    for i in range(len(numbers)):
        product *= numbers[i]
        answer.append(product)
    return answer

def right(numbers:list[int]) -> list[int]:
    answer = []
    product = 1
    numbers = numbers[::-1]
    for i in range(len(numbers)):
        product *= numbers[i]
        answer.append(product)
    return answer
"""
"""
Attempt 2
def productExceptSelf(nums: list[int]) -> list[int]:
    
    lengthOfArray = len(nums)
    print("nums = ",nums)
    
    # leftArray = left(nums)
    leftArray = getProduct(nums,0,lengthOfArray-1)
    
    print("left array = ",leftArray)
    
    # rightArray = right(nums)
    rightArray = getProduct(nums,lengthOfArray-1,-1)
    
    print("right array = ",rightArray)
    
    answer = []
    
    if lengthOfArray == 0:
        return nums
    
    for i in range(lengthOfArray):
        if i == 0:
            answer.append(rightArray[lengthOfArray-2])
        elif i == lengthOfArray-1:
            answer.append(leftArray[lengthOfArray - 2])
        else:
            answer.append(leftArray[i-1]*(rightArray[::-1][i+1]))
        #print(answer)
    
    return answer


def getProduct(nums:list[int],start:int,end:int) -> list[int]:
    product = 1
    answer = []
    step = -1 if start > end else 1
    for i in range(start,end,step):
        product *= nums[i]
        answer.append(product)
    return answer

print(productExceptSelf([1,2,3,4]))
"""

# getProduct(list,firstIndex,lastindex) if start < end
# getProduct(list,lastIndex - 1,-1) if start > end
# print(getProduct([4,3,2,1,2],0,5))
# print(getProduct([4,3,2,1,2],4,-1))


"""
Attempt 3
def productExceptSelf(nums:list[int]) -> list[int]:
    answer = []
    lengthOfArray = len(nums)
    for i in range(lengthOfArray):
        answer.append(getProduct(nums,0,i) * getProduct(nums,i+1,lengthOfArray))
    
    return answer

def getProduct(nums:list[int],start:int,end:int) -> int:
    product = 1
    for i in range(start,end):
        product *= nums[i]

    return product

print(productExceptSelf([-1,1,0,-3,3]))
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
    # alredy contains the prefix values, 
    # hence eliminating the need for an extra array 
    # postfix = 
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= postfix
        postfix *= nums[i]

    return answer

print(productExceptSelf([1,2,3,4]))