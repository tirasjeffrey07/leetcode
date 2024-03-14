"""
if nums[0]==1:
    for index,value in enumerate(numbers):
        if (index+1) != value:
            return [value,index+1]
else:
    for index,value in enumerate(numbers[::-1]):
        if (index+1) != value:
            return [value,index+1]


"""

"""
My try
numbers = [2,3,2]
def findErrorNums(nums: list[int]) -> list[int]:
    n = len(numbers) + 1


    track={}
    for i in range(1,n):
        track.__setitem__(i,nums.count(i))
        # {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1}
    ans = [-1,-1]
    for i,j in track.items():
        if j  == 2:   
            ans[0] = i
        if  j==0:
            ans[1] = i
    return ans"""
    

from collections import Counter


print(Counter([1,2,2,4,4,4]
))

numbers = [2,3,2]
count = Counter(numbers)

ans=[0,0]

for number in range(1,len(numbers)):
    if count[number] == 2:
       ans[0] = number
    if count[number] == 0:
        ans[1] = number

print(ans) 