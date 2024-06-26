"""
leet - 238

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 
--------------------------------------
Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
--------------------------------------
Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9
--------------------------------------


Simply represent the  ranges as strings and return them.
The ranges might be continuous like 0,1,2,3 (return ["0->3"])
or
broken like 0,1,2,6,9,10 (return ["0->2", "6", "9->10"])


Approach:
1) have a start and end value (initially first value)
2) start iterating from index 1 to len(array) - 1
3)
if array[index] > end + 1:
    if start == end
        add "start->end" to the answer
    else:
        add "start" or "end" to the answer (both are same)
else:
    update end to array[index]

do this till the index reaches the end

"""



def summaryRanges(self, nums: list[int]) -> list[str]:
    if not nums:
        return []
    res = []
    start, end = nums[0], nums[0]

    for i in range(1, len(nums)):
        if nums[i] > end + 1:
            if start == end:
                res.append(f"{start}")
            else:
                res.append(f"{start}->{end}")
            start, end = nums[i], nums[i]
        else:
            end = nums[i]

    # we will still have a range after exitting the loop
    if start == end:
        res.append(f"{start}")
    else:
        res.append(f"{start}->{end}")
    
    return res


            


    