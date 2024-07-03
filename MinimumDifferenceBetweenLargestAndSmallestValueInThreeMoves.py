"""
leetcode 1509
POTD - 3/7/24

You are given an integer array nums.

In one move, you can choose one element of nums and change it to any value.

Return the minimum difference between the largest and smallest value of nums after performing at most three moves.

 
----------------------------------------------------------------------

Example 1:

Input: nums = [5,3,2,4]
Output: 0

Explanation: We can make at most 3 moves.
In the first move, change 2 to 3. nums becomes [5,3,3,4].
In the second move, change 4 to 3. nums becomes [5,3,3,3].
In the third move, change 5 to 3. nums becomes [3,3,3,3].
After performing 3 moves, the difference between the minimum and maximum is 3 - 3 = 0.

----------------------------------------------------------------------

Example 2:

Input: nums = [1,5,0,10,14]
Output: 1

Explanation: We can make at most 3 moves.
In the first move, change 5 to 0. nums becomes [1,0,0,10,14].
In the second move, change 10 to 0. nums becomes [1,0,0,0,14].
In the third move, change 14 to 1. nums becomes [1,0,0,0,1].
After performing 3 moves, the difference between the minimum and maximum is 1 - 0 = 1.
It can be shown that there is no way to make the difference 0 in 3 moves.

----------------------------------------------------------------------

Example 3:

Input: nums = [3,100,20]
Output: 0

Explanation: We can make at most 3 moves.
In the first move, change 100 to 7. nums becomes [3,7,20].
In the second move, change 20 to 7. nums becomes [3,7,7].
In the third move, change 3 to 7. nums becomes [7,7,7].
After performing 3 moves, the difference between the minimum and maximum is 7 - 7 = 0.

----------------------------------------------------------------------

understanding the problem statement...

given an array, we need to return the difference between min and max elements after changing any 3 elements


Approach:
O(NlogN) time and O(1) space 

- since we are finding a value related to min and max, it is best to sort the array.
- whenever we are finding the difference between min and max it only involves the first and last element (since it's sorted)
- we are given that we can only perform 3 changes (to any element in the array)
- since the difference involves only the first and the last elements, we need to change 3 elements at the front or at the back

we will look at the following examples (always sort the array first)
1) [1,2,3,4]

    length is 4, so doesnt matter what 3 elements we change, the difference will be 0
    
    [4,4,4,4] change first 3 elements to 4, diff bw min and max will be 0
    
    [1,1,1,1] change the last 3 to 1, diff will still be 0

so the problem arises only when the number of elements in the array is more than 4... (this is our base return case)

2) [1,2,4,8,12]

    the diff is 12 - 1 = 11, we need to reduce it

    1st - say we remove 12, the diff becomes 8 - 1 = 7
    2nd - say we remove 8, the diff becomes 4 - 1 = 3
    3rd - say we remove 4, the diff becomes 2 - 1 = 1

    return 1

How do we know from which end we remove the elements?

We already now that we cna only remove 3 elements? What are the ways in which we can remove three elements?
        
array                [1,2,4,8,12]

number               0         3         we remove 0 elements from the left &  [4,8,12] from right, diff =  2 - 1  
of removals          1         2         we remove [1] from left &  [8,12] from right, diff = 4 - 2 
                     2         1         we remove [1,2] from left &  [12] from right, diff = 8 - 4       
                     3         0         we remove [1,2,4] from left & 0 elements from right, diff = 12 - 8

These are all possible combinations in every array...

Have two pointers, i and j
i goes from 0 to 3
j goes from 3 to 0

calculate the diff and return the min among them
"""
from collections import List

def minDifference(self, nums: List[int]) -> int:
    n = len(nums)
    i = 0 # left cut off indicator
    j = 3 # right cut off indicator
    
    if len(nums) <= 4:
        return 0
    
    nums.sort()

    diff = float('inf')
    
    while i <= 3 and j >= 0:
        #                right value       left value
        diff = min(diff, nums[n - 1 - j] - nums[i])
        # checkout all possible combinations
        i += 1
        j -= 1

    return diff