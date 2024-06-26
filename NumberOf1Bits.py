"""
Given an integer representation of a binary sequence return the number of set bits (1)

IP = 11
OP = 3

My approach:
Put the binary string into the Counter constructor, return the value of key "1"

Proper approach:
Take the right most bit, AND it with 1
1 & 1 = 1 (if this is the case increment counter, right shift N by 1 to check the next digit towards the left)
1 & 0 = 0 (do nothing, just skip)

num_bits = 0
    while n:
        if n & 1:
            num_bits += 1
        
        n >>= 1
    return num_bits

"""
from collections import Counter

def hammingWeight(self, n: int) -> int:
        return Counter(bin(n)[2:])["1"]

