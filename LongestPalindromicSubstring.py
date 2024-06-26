
"""

Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.


--------------------------------------------------
Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
--------------------------------------------------
Example 2:

Input: s = "cbbd"
Output: "bb"
--------------------------------------------------

Constraints:

1 <= s.length <= 1000


Naive Approach:                                               Time Complexity
- Find each and every substring                                   O(N²)
- Check if each and every substring is a palindrome or not        O(N)   x
                                                               -----------
                                                                  O(N³)

Optimal Approach:
- Typically we check if a string is palindrome by using both extremes and converging towards the center index using left and right pointers
- But what if, for a string s, we started from the middle, explored outwards comparing left and right positions till either reaches their respective ends?
eg:      bababba
        l<--i-->r
        l<---i->r

- for each index, we do this
- but for even number of characters, we have to check from either i, i+1 or i-1, i, but we do the former since we start from the 0th index


"""



def longestPalindrome( s: str) -> str:
    maxPal = ""
    maxLen = 0
    n = len(s)

    for i in range(n):
        # checking for odd length palindromes
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            # if len of the palindrome greater than max length, update it
            if (r - l + 1) > maxLen:
                maxLen = r - l + 1
                maxPal = s[l:r+1]
            l -= 1  # dont forget it
            r += 1  #  "     "
        
        # checking for even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            # if len of the palindrome greater than max length, update it
            if (r - l + 1) > maxLen:
                maxLen = r - l + 1
                maxPal = s[l:r+1] 
            l -= 1  # important
            r += 1  #    "
    return maxPal