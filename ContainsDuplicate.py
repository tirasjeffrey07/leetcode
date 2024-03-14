
"""
Problem return True if the given array contains duplicates 
else return False

def containsDuplicates(nums:list[int])->bool:
    if len(set(nums)) == len(nums):
        return True
    return False
"""
def containsDuplicate(self, nums: list[int]) -> bool:
    return (False if len(set(nums))==len(nums) else True)

"""
Can be optimised as:

def containsDuplicates(self,nums:List[int]) -> bool:
    return len(set(nums)) != len(nums)

"""