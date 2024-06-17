
"""
Logic behind the formula: n(n-1)/2

We have to fill two slots 

say we have 4 1's

[1, 1, 1, 1]    

    4 3
    _ _

we have 4 ones for the first slot and (4-1) ones for the second slot
so 4*3 = 12 good pairs

however, we would also take pairs like [3,1], [2,1] which are invalid since 'i' is not < 'j'

so, for each pair (where i < j) we would also have the same pair but the elements would be in different slots

hence, to negate that issue, we simply divide it by two since every pair undergoes this effect

so for the above example we would have, 4 * 3 // 2 = 6 valid pairs

"""

from collections import Counter

def numIdenticalPairs(nums: list[int]) -> int:
    number = 0

    if len(nums) == 1:
        return 0

    newNums = Counter(nums)
    
    # naive solution
    
    # for i in range(0, len(nums) - 1):
    #     for j in range(i+1, len(nums)):
    #         if nums[i] == nums[j] and i < j:
    #             number += 1
    
    for _, v in newNums.items():
        if v > 1:
            number += (v*(v-1)) // 2

    return number