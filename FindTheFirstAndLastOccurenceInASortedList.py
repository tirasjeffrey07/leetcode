class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1

        start = 0
        end = len(nums) - 1

        # finding the first occurence
        while start <= end:

            mid_loc = (start + end) // 2
            result = findStartingPosition(nums, target, mid_loc)
            # meaning search the left sub array
            if result == "left":
                end = mid_loc - 1
            # meaning search the right sub array
            elif result == "right":
                start = mid_loc + 1

            elif result == "found":
                first = mid_loc
                break
        
        # resetting conditions for the next binary search of the last element
        start = 0
        end = len(nums) - 1
        
        # finding the ending position
        while start <= end:

            mid_loc = (start + end) // 2
            result = findEndingPosition(nums, target, mid_loc)
            # meaning search the left sub array
            if result == "left":
                end = mid_loc - 1
            # meaning search the right sub array
            elif result == "right":
                start = mid_loc + 1

            elif result == "found":
                last = mid_loc
                break
        
        return [first,last]

def findEndingPosition(array, key, mid_loc):
    print("mid:", mid_loc, " array[mid]:", array[mid_loc])
    if key == array[mid_loc]:
        # check if righter-er val is also key
        # but dont go out of bounds
        if mid_loc < len(array) - 1 and array[mid_loc + 1] == key:
            return "right"
        # if not first match is found
        else:
            return "found"
    elif key < array[mid_loc]:
        return "left"
    else:
        return "right"


def findStartingPosition(array, key, mid_loc):
    print("mid:", mid_loc, " array[mid]:", array[mid_loc])
    if key == array[mid_loc]:
        # check if left-er val is also key
        # but dont go out of bounds
        if mid_loc > 0 and array[mid_loc - 1] == key:
            return "left"
        # if not first match is found
        else:
            return "found"
    elif key < array[mid_loc]:
        return "left"
    else:
        return "right"
