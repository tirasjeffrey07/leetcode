"""
2465. Number of Distinct Averages

You are given a 0-indexed integer array nums of even length.

As long as nums is not empty, you must repetitively:

1) Find the minimum number in nums and remove it.
2) Find the maximum number in nums and remove it.
3) Calculate the average of the two removed numbers.
    The average of two numbers a and b is (a + b) / 2.

For example, the average of 2 and 3 is (2 + 3) / 2 = 2.5.

Return the number of distinct averages calculated using the above process.

Note that when there is a tie for a minimum or maximum number, any can be removed.

 

---------------------------------------------------------------------------------
Example 1:
Input: nums = [4,1,4,0,3,5]
Output: 2

Explanation:
1. Remove 0 and 5, and the average is (0 + 5) / 2 = 2.5. Now, nums = [4,1,4,3].
2. Remove 1 and 4. The average is (1 + 4) / 2 = 2.5, and nums = [4,3].
3. Remove 3 and 4, and the average is (3 + 4) / 2 = 3.5.
Since there are 2 distinct numbers among 2.5, 2.5, and 3.5, we return 2.

---------------------------------------------------------------------------------
Example 2:
Input: nums = [1,100]
Output: 1

Explanation:
There is only one average to be calculated after removing 1 and 100, so we return 1.
---------------------------------------------------------------------------------
 

Constraints:

2 <= nums.length <= 100
nums.length is even.
0 <= nums[i] <= 100

Approach:
- Average involves computation using the min and max each time
- So we sort the array first (O(NlogN))
- Now the max is the last value, min is the first
- Use two pointers, i = 0 and j = length of array - 1
- At each iteration, add the array[i] (min value) and array[j] (max value), divide it by 1 and add it to a set
- We simply include every average to the set since set cant hold dupes, it simply wont add it if an AVG value is already exists there
- increment i, decrement j (min and max val gets updated)
- repeat till i and j meet (ie at the middle)
"""


from collections import List

def distinctAverages(self, nums:List[int]) -> int:
        
        nums.sort()
        avgs = set()

        i,j = 0, len(nums) - 1 
        
        while i <= j:
            avgs.add( (nums[i] + nums[j]) / 2 )
            i+=1
            j-=1

        return len(avgs) 