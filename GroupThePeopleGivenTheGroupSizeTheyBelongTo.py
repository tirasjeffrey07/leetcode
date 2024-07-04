"""

Leetcode 1282

Group the People Given the Group Size They Belong To


There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

-----------------------------------------------------------------------------------

Example 1:

Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]

Explanation: 
The first group is [5]. The size is 1, and groupSizes[5] = 1.
The second group is [0,1,2]. The size is 3, and groupSizes[0] = groupSizes[1] = groupSizes[2] = 3.
The third group is [3,4,6]. The size is 3, and groupSizes[3] = groupSizes[4] = groupSizes[6] = 3.

Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].

-----------------------------------------------------------------------------------

Example 2:

Input: groupSizes = [2,1,3,3,3,2]
Output: [[1],[0,5],[2,3,4]]

-----------------------------------------------------------------------------------

Understanding the problem...

- Given an array, each index in that array is a person
- Each person belongs to a group
- The value at that index denotes the size of the group to which that person belongs
- Now our job is to, split the given array, into groups
- Each group is represented by a list
- Each value in a group is a person (index)

Lets take example 2,

[2,1,3,3,3,2]

person 0 (which is the index) is in a group of 2 (value at the index)
similarly,,,
p1 is in g(1)
p2 is in g(3)
p3 is in g(3)
p4 is in g(3)
p2 is in g(2)

How do we approach this?

The only easily understandable way is probably using hashmap

We will take the group sizes as key, indices as values
Values will be stored in a list

1) Take each element in the array (size of the group)
2) Put it in the hashmap as a key if it doesnt exist
3) If the element (size) already exists, append/push the index (person, which is the value) to the size (which is the key)
4) Before appending, check if we add that element to that specific size list, will it be the same size  as the group size? If yes, append that entire list + the current element to the answer list
    
   Explaining pt 4:
    
    take [3,3,3,3,1,1]
    
    consider this condition =>   [3,3,3,3,1,1]
                                      i
    At this point this is how our hashmap & result array would look..
    
    res = []
    hashmap = {
        3 : [0,1]
    }                 

    if we add i (= 2) to the list ( hashmap[ array[i] ] ), it will be equal to the size of the group (array[i])
    so we do this, we append hashmap[array[i]] + i to the result and reset the list

    which will then look like this:

    hashmap = {
        3 : []
    }                 
    res = [0,1,2]


"""
from typing import List

def groupThePeople( groupSizes: List[int]) -> List[List[int]]:
    hashmap = {}
    res = []
    for i, val in enumerate(groupSizes):

        # group of len = 1, directly append it as a single element list
        if val == 1:
            res.append([i])
        
        if val in hashmap:
            # current len of the value == val - 1
            # 
            # val = 3
            # 
            # { 
            #   3 : [0,1]
            # }   
            
            if len(hashmap[val]) == val - 1:
                res.append(hashmap[val] + [i])
                hashmap[val] = []
            
            # append to the list
            else:
                hashmap[val].append(i)
        else:
            hashmap[val] = [i]

    return res