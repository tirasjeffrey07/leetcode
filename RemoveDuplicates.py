"""
The objective is to remove duplicates from a sorted array

function should return the number of unique elements
"""



def removeDuplicates(nums:list[int]) -> int:
    index = 0
    # we start checking only from the second element coz 
    # first element is always unique
    # only the second element may be the copy of the first one
    index = 1
    for i in range(len(nums) - 1):
        # index will hold the array index of the last unique element
        if nums[i] != nums[i+1]:
            nums[index] = nums[i+1]
            index += 1
    return index


# we know that the array is sorted which means that
# if ith number is greater than (i-1)th number, then ith 
# number is unique we use the same principle to keep update i
# to the further most index where the element is greater

# if the 2nd element is greater than the first element
# the first element is unique


# say arr = [1,2,2,2,2,2,4,4,5,6,7] 
# index = 1
# if arr[0] != arr [1]
# means that they are unique elements
# so we swap the index element with arr[2]