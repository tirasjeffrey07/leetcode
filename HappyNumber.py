"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.

Repeat the process until the number equals 1 (where it will stay ie get looped again and again), or it loops endlessly in a cycle which does not include 1.

Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
Example 2:

Input: n = 2
Output: false
Explanation:
2^2 = 4    <----------
4^2 = 16             |
1^2 + 6^2 = 37       |
3^2 + 7^2 = 58       | 
5^2 + 8^2 = 89       |
89 -> 145            |
145 -> 42            |
42 -> 20             |
20 -> 4    -----------

we reach 4 again, so compute squares till the sum reaches 1 
if we encounter a sum that has already been visited return False
"""

def isHappy(self, n: int) -> bool:
    visited = set() # keep track of all the previously calculated sums

    while n not in visited:
        visited.add(n)
        
        # helper to calulcate sum
        n = self.sumOfSquares(n)

        if n == 1:
            return True
        
    def sumOfSquares(self, n) -> int:
        sum = 0  
        while n != 0:
            r = n % 10
            sum = sum + (r * r)
            n = n // 10
        return sum