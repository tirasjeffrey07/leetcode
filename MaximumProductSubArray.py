"""
Given an integer array "nums", find a subarray that has the largest product, and return the product.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


We use dynamic programming to solve this
Keep track of both the MAX product subarray and the MIN product subarray
Individual elements are also subarrays

case 1:
If the numbers are all positive, no matter the number, the product will always increase
case 2:
If the numbers are all negative, if number of elements is even then the product will increase, 
if its odd itll end up being a negative number
eg:
[-1,-2,-3] -6 is the product of all elments, but the solution is -2,-3 which give us 6
First calculate the max product of the first two elements also calculate the minimum product

[-1,-2,-3]
maxSub(-1,-2) = max = 2
minSub(-1,-2) = min = -2

next element is -3
max * -3 = -6
min * -3 = +6
now min is -6 and max is +6

say our array is [-1,-2,-3,-4 or +4]
max = 6
min = -6

we'll be able to find the answer no matter what as we both max and min to use,
max * 4 = 24
min * -4 = 24

Case 3:
0 value
when we encounter a 0, we reset the min and max to 1 
so the product gets neutralised
"""

def maxProduct(nums: list[int]) -> int:
    # if the list contains only 1 number, 
    # thats the max element
    res = max(nums)
    currMax, currMin = 1, 1

    for number in nums:
        # if the number we encounter is 0, we reset min and max
        if number == 0:
            currMin, currMax = 1, 1
            continue

        # using temp to get the value of the currMax before it gets possibly reassigned
        temp = currMax * number

        # the max maybe the number itself, 
        # if the number is negative we use min to get max product (currMin * number) -2 * -3 = 6  
        # if the number is postive we use max to get max product (currMax & number) 2 * 3 = 6 
        currMax = max(number * currMax, number * currMin, number)

        # the min maybe the number itself
        # if the number is positive we use min to get the min value (currMin * number) -2 * 3 = -6
        # if the number is negative we use max to get the min value (currMax * number) 2 * -3 = -6
        currMin = min(temp, number * currMin, number) 

        # getting the result
        res = max(res,currMax)

    return res

print(maxProduct([2,3,-2,4]))