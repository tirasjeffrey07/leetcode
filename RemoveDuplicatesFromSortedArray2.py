"""
LC - 80


Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice.

The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. 

More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 

It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

!!! Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory. !!!

this is same as the first part, but in this array an element can have atmost TWO duplcates



This was my successful approach, i used sort() function at the end, this is not the right way to do it even it was accepted and efficient !!!

def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i, j = 0, 1
        count = 1
        infCount = 0
        while i <= j and j < len(nums):
            if nums[i] == nums[j]:
                count += 1
                if count > 2:
                    nums[j] = float("inf")
                    infCount += 1
                j += 1
            # if nums[i] != nums[j]
            else:
                i = j
                count = 1
                j += 1
        # nums = sorted(nums)[:len(nums) - infCount] throw a casting error
        nums.sort()
        return len(nums) - infCount
"""


# this is the proper approach with the correct 2 pointer concept

from collections import List

def removeDuplicates(self, nums: List[int]) -> int:
        # left is for replacement, right is for finding the steak of duplicates
        l, r = 0, 0

        while r < len(nums):
            # base count for every number
            count = 1
            
            while r +  1 < len(nums) and nums[r] == nums[r+1]:
                # keep going on to find the end of the duplicate streak
                r += 1
                count += 1
            # this loop is for shifting (copying actually)elements to the left
            for _ in range(min(2, count)): # 1 or 2 times
                nums[l] = nums[r]
                l+=1
            # move to the next element after shifting elements
            r += 1
        return l
"""
n = 8 
1 1 1 2 2 2 3 3 

at the end this is how itll be
1 1 2 2 3 3 3 3 
            l
            r
l will be at 6, so we return 6 i.e first k (which is 6) elements are without duplicates

"""
