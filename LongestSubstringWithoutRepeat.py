"""
Given a string s, find the length of the longest 
substring
 without repeating characters.

 
----------------------------------------------------------
Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

----------------------------------------------------------
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

----------------------------------------------------------
Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

def lengthOfLongestSubstring(self, s: str) -> int:
    if len(s) == 1 or len(s) == 0:
        return len(s)

    # left, right set  to 0
    i, j = 0, 0
    hashset = set()

    maxLen = 0
    # moving right pointer till the end of the string
    for j in range(len(s)):
        # if the right pointer val is already present
        while s[j] in hashset:
            # remove left pointer value coz it already exists in the hashset
            hashset.remove(s[i])
            # move left pointer
            i += 1
        hashset.add(s[j])
        maxLen = max(maxLen, j - i + 1)
    return maxLen 