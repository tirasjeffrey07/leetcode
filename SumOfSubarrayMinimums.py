"""
Leetcode 907
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
"""

# Incomplete, trying to calculate all subarrays of the array
"""
def sumSubArrayMins( arr: list[int]) -> int:
    n= len(arr)
    subArrays,minSumOfSubArray=[],0
    for i in range(n):
        temp = []
        for j in range(n-i-1,i-1,-1):
            temp.append(arr[j])
            print(temp)
        minSumOfSubArray+= min(temp)
        subArrays.append(temp)
    return minSumOfSubArray

 sumSubArrayMins([0,1,2,3])
"""


def sumSubArrayMins(arr: list[int]) -> int:
    MOD = 10**9 + 7
    res = 0
    stack = []  # stores (index,num)

    for i, n in enumerate(arr):
        # checking if the stack is empty -1 is top [1] holds the value
        # checking for stack as well, coz it maybe empty
        while stack and n < stack[-1][1]:
            # popping the element and catching it
            j, m = stack.pop()

            #   j     i
            # 1,2,3,4,1

            left = (
                j - stack[-1][0] if stack else j + 1
            )  # grabbing index of the element to the left of j

            right = i - j

            res = (res + m * left * right) % MOD
        stack.append((i, n))

    for i in range(len(stack)):
        j, n = stack[i]
        left = j - stack[i - 1][0] if i > 0 else j + 1
        right = len(arr) - j
        res = (res + n * left * right) % MOD
    
    return res
