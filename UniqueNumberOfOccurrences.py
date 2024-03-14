"""
1207. Unique Number of Occurrences

Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.


Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

"""


from collections import Counter


def uniqueOccurrences(arr: list[int]) -> bool:
    dic = {}
    # dic{number:array.count(number)}
    for num in arr:
        dic.__setitem__(num, arr.count(num))
        # or dic[num] = arr.count(num)
    # number of unique values ==  number of values()
    if len(dic.values()) == len(set(dic.values())):
        return True
    return False


print(uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))

x = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]

# cntr = Counter(x)
# print(cntr)
# if len(cntr.values()) == len(set(cntr.values())):
#     print("True")
# else:
#     print("False")
# Counter() automatically creates a dictionary with values as keys and their count() as values