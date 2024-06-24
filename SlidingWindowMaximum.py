"""
Sliding Window Maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.


Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


"""


from collections import deque
from collections import List

def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

    # monotonic decreasing queue so all elements will be in decreasing order
    q = deque() # we just store indices here

    l, r = 0, 0
    res = []

    while r < len(nums):

        # before appending, remove all values smaller than nums[r]
        while q and nums[q[-1]] < nums[r]:
            q.pop()

        # add the nums[r] now, actually just the index
        q.append(r)

        # when the window moves, pop the left most value to update deque
        if l > q[0]:
            q.popleft()

        # size of the window must be atmost k
        if (r + 1) >= k:
            
            # if it is greater than k
            # add the left most value to the res
            res.append(nums[q[0]])

            # move left pointer so the window moves
            l += 1

        r += 1
    return res