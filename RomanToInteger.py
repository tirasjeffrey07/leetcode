"""
Convert the given roman number to integer
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


def romanToInt(romanNumber: str) -> int:
    romanMap = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    n = len(romanNumber)
    # stores the int value of the last element of the roman value
    num = romanMap[romanNumber[n-1]]
    # start moving from left to right in the reverse order starting from the second last
    for i in range(n-2,-1,-1):
        # eg: if V is greater than I  add V to the sum
        if romanMap[romanNumber[i]] >= romanMap[romanNumber[i+1]]:
            num += romanMap[romanNumber[i]]
        # eg: if I is lesser than V, subtract I from V 
        else:
            num -= romanMap[romanNumber[i]]
    
    return num    


print(romanToInt("MMMCDXC"))