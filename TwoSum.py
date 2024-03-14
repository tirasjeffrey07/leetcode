def solution(nums:list[int],target:int) -> list[int]:
    hashmap =dict() # or use {}
    
    # enumerate is equivalent to a dictionary with indices
    # as keys starting from 0 to n and has values as values
    
    for i,value in enumerate(nums):
        if target - nums[i] in hashmap:
            return [i,hashmap[target-nums[i]]]
        hashmap[value] = i
    
print(solution([2,7,11,15],9))

"""
Logic:
For a given input array this algorithm does the following steps:

Create a hashmap which stores integer  as key(number) and value(its index).

Iterate through each element in the given array starting from the first element.

In each iteration check if required number (required  number = target sum - current number) is present in the hashmap.

If present, return {required number index, current number index} as  result.

Otherwise add the current iteration number as key and its index as value to the hashmap. Repeat this  until you find the result.

"""