
"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

---------------------------------
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
---------------------------------
Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
---------------------------------
Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
---------------------------------


- Sliding Window of len k + 1
- check if number if already there in hashset
- if yes return True
- else, move right in the window and do the same
- if window is about to be crossed, move window to the right (move left limit, remove left element from the set)


"""

def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        
        hashset, l = set(), 0


        for r in range(len(nums)):
            
            if r - l > k:
                # remove left element since window is moving right
                hashset.remove(nums[l])
                l += 1


            # check if we have already come across this number
            if nums[r] in hashset:
                return True
            
            # if none of the above trigger anything, add this number since its not seen b4
            hashset.add(nums[r])
        return False