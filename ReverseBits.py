"""
Given a 32 bit integer
return the reversed value

"""


def reverseBits(self, n: int) -> int:
    res = 0 # left shift the result every time you update the bit
    for i in range(32):
        # shift the number to the right by i so we can get the i-th bit
        # by ANDing it with 1
        bit = (n >> i) & 1

        # we need to update res in the reverse order
        # so we move the resultant bit left from the end each time
        res = res | (bit << ( 31 - i))
    return res
""" 
String method
1) Convert int to binary, remove '0b' prefix
2) Left fill with 0s using zfill to make sure its 32
3) Reverse the string
4) return int of the string repr

    binary_representation = bin(n)[2:].zfill(32)
    
    reversed_binary = binary_representation[::-1]
    
    return int(reversed_binary, 2)
"""