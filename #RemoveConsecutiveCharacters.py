"""
Given a string S. For each index i(1<=i<=N-1), erase s[i] if it is equal to s[i-1] in the string.

-----------------------------------------------
Example 1:
-----------------------------------------------
Input:
S = aabb
Output:  ab 
Explanation: 
'a' at 2nd position is
appearing 2nd time consecutively.
Similiar explanation for b at
4th position.

-----------------------------------------------
Example 2:
-----------------------------------------------

Input:
S = aabaa
Output:  aba
Explanation: 
'a' at 2nd position is
appearing 2nd time consecutively.
'a' at fifth position is appearing
2nd time consecutively.

"""

def removeConsecutiveCharacter(S) -> str:
    if len(S) == 1:
        return S
    
    res = ""
    i = 0
    while i < len(S):
        # first append the char
        res += S[i]
        
        # move pointer till you reach the last recurring char
        while i + 1 < len(S) and S[i] == S[i+1]:
            i += 1
            
        i += 1
            
    return res