"""
leetcode 41

First Missing Positive

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

-------------------------------------------------------------------------------
Example 1:

Input: nums = [1,2,0]
Output: 3

Explanation: The numbers in the range [1,2] are all in the array.
-------------------------------------------------------------------------------
Example 2:

Input: nums = [3,4,-1,1]
Output: 2

Explanation: 1 is in the array but 2 is missing.
-------------------------------------------------------------------------------
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1

Explanation: The smallest positive integer 1 is missing.



Approach:

The definition of this problem is quite misleading, I'll try my best to explain it...

assume there's a number 'n'
there's an array of size 'n'


there are two cases we have to consider:
1) array having all the numbers from the range 1 - n 
2) array missing some (could be all) numbers from the range 1 -  n

case 1:
if the array has all the numbers from 1 to n, it is obviously full as it has exaclty n spaces.
if this is the case, return n + 1

case 2:
if the array has some missing elements from the range 1 to n, there are other useless elements filling that space
among the missing elements from the range 1 to n, return the smallest


My approach:
put all the elements from one to n in a hashset
iterate through the given array, for each number, 
remove that same number from the hashset 
by the end, if there are any numbers left in the hashset, return the min of it
else return n + 1
"""


from collections import List

def firstMissingPositive(self, nums: List[int]) -> int:
    n = len(nums)
    numRef = set([x for x in range(1,n+1)]) # O(Nf not O(1))
    for num in nums:
        if num in numRef:
            numRef.remove(num)
    if numRef:
        return min(numRef)
    if not numRef:
        return n+1