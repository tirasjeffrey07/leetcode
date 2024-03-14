"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
"""




"""
-------
Theory
-------


Sorted array means that in most cases ull be 
using Binary Search, here its a modified 
version of binary search

rotating [1,2,3,4,5] 1 time would result in [5,1,2,3,4]

in an array of N integers, if the array is rotated N times, 
it means that the final array is the same as the original array 

if thats the case we just return the first element since the 
first element is the smallest element in a sorted array

eg: consider array [3,4,5,1,2]
notice how element[i+1] > element[i], except 5,1 
so we find the position where this happens and the value 
next to it the smallest value

refer https://www.youtube.com/watch?v=nIVW4P8b1VA&t=385s
for breakdown

first we check if the middle (length / 2) value is part of the left sorted array (3,4,5) or right sorted array (1,2).

any rotated array can be divided into left sorted array and right sorted array

if the middle element is part of the left sorted array, we only search 
for the element in the right sorted array as all the values to the left will be smaller

if nums[middle] >= nums[leftMostIndex] then the middle element belongs to the left sorted array

but if the middle was in the right sorted array then we only need 
to search the left part of the array as all elements towards the right will be greater
"""

def findMin(nums: list[int]) -> int:
    
    left,right=0,len(nums) - 1
    # arbitrary result to store the result
    res = nums[0]

    while left<=right:
        
        # if the entire array is sorted already
        if nums[left] < nums[right]:
            # picking te left most as its the smallest
            res=min(res,nums[left])
            break
        
        mid = (right+left) // 2
        res = min(res,nums[mid])
        
        # if the mid value belongs the left sorted array
        if nums[mid] >= nums[left]:
            # search only the right by altering the left index
            left = mid + 1
        # else if the mid value belongs to the right sorted array
        else:
            # search only the left by altering the right index
            right = mid - 1
    return res


"""
optimised code:

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1 
        answer = float("inf")
        
        while left < right:
            mid = (left + right) // 2
            answer = min(answer, nums[mid])
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1 
                
        return min(answer, nums[left])
"""

        
    