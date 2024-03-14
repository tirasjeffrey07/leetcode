"""
leet 1239
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
 
Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26

"""


# def maxLength(arr: list[str]) -> int:
#     maxLen = 0
#     if len(arr) == 1:
#         return len(arr[0])
#     for i in range(len(arr) - 1):
#         for j in range(len(arr)):
#             if j == i:
#                 continue
#             temp = list(arr[i] + arr[j])
#             if len(temp) == len(set(temp)):
#                 if len(temp)>maxLen:
#                     maxLen = len(temp)

#     return maxLen

# print(maxLength(["abcdefghijklmnopqrstuvwxyz"]))

"""
Doesnt work !!!
def maxLength(self,arr:list[str]) -> int:
    # using a set to keep track of all the strings added 
    #["un","iq","ue"]
    n = len(arr)
    # well perform dfs recursively till you
    def dfs(i, track:set()):

        self.output = 0
        # base case: if we've reached the end of the array
        if i == n:
            # update output to the max of previous outputand the length of the max length string
            self.output =  max(self.output,len(track))

        # iterating through every word from i to last
        for j in range(i,n):
            # temp set to add letters
            current = set()
            # if the word itself doesnt contain any dupes
            if len(arr[j])==len(set(arr[j])):
                # iterating through every character of the current word 
                for c in arr[j]:
                    # if char is already in the set of letters so far, reset current
                    if c in track:
                        # reset temp set
                        current = set()
                        break

                    # else add the current letter to tracking set
                    track.add(c)

                # move on to the next word combining both the tracking set and current valid strings
                dfs(j+1,track|current)
    # initial call starting from index 0 and an empty set
    dfs(0,set())

    return self.output
    """
from collections import Counter


def maxLength(arr: list[str]) -> int:
    charSet = set()

    # used to check if theres any overlap characters between
    # the current string and the set of valid characters
    def overlap(charSet, s):
        # itll work for cases like
        # charSet = "", s = "bb"
        c = Counter(charSet) + Counter(s)

        # returns true if the count of all characters is 1
        return max(c.values()) > 1

    def backtrack(i):
        # base case: return len of all characters
        # added if we reach the end of the array
        if i == len(arr):
            return len(charSet)

        res = 0

        # if theres no overlap
        if not overlap(charSet, arr[i]):
            # iterate through all letters of the current word and add them to the set
            for char in arr[i]:
                charSet.add(char)

            # move forward by one string and do the same
            # calling backtrack(next_word) with adding the characters of teh current word
            res = backtrack(i + 1)

            for c in arr[i]:
                charSet.remove(c)
            # calling backtrack(next_word) without adding the characters of the current word
        return max(res, backtrack(i + 1))

    # initial call with index as 0
    return backtrack(0)
