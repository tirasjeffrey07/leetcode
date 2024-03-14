"""
Longest Common Prefix


Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longestCommonPrefix( strs: list[str]) -> str:
        # using the first string as the reference
        answer = ""
        smallest = min(strs,key=len)
        minLength = len(smallest)
        # iterate through the index of the smallest string
        for i in range(minLength):
            
            # Get the current character from the first string
            current = strs[0][i]
            
            # Check if this character is found in all other strings or not
            for j in range(0, len(strs)):
                if strs[j][i] != current:
                    return answer
            answer += current
        return answer


print(longestCommonPrefix(["flower","flow","flight"]))

# print(min(["flower","flow","flight"],key = len))



"""
Fastest solution:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs)
        i = 0
        j = len(smallest)
        while i < len(strs):
            if strs[i].startswith(smallest[0:j]):
                i+=1
            else:
                j-=1
                i = 0
        if len(smallest[0:j]) > 0:
            return smallest[0:j]
        else:
            return ""

"""
