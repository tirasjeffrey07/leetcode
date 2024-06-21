"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all NON-ALPHANUMERIC characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

"""


# what i did

def isPalindrome( s: str) -> bool:
        formattedString = ""
        for c in s:
            if c.isalnum():
                formattedString += c.lower()

        start = 0 
        end = len(formattedString) - 1
        
        while start <= end:
            if formattedString[start] == formattedString[end]:
                start += 1
                end -= 1
            else:
                return False
        return True



# whats efficient time and space wise:
def isPalindrome(s: str) -> bool:
        l=0
        r=len(s)-1

        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower() == s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True