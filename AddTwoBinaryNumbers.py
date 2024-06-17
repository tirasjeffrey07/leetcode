"""
Add two binary numbers and return the sum

My approach:

1) Check if both strings are the same length
2) If they are not, find the difference in len, lets call it diff
3) add diff times "0" to the front of the shorter string
4) iterate over each char in the string using a while loop, keep track of the carry
5) check if theres a remaining carry in the end, add it to the front


One line solution:

return bin(int(a,2) + int(b, 2))[2:]

- int(value, base)
- bin() returns binary value with the prefix 0b

"""


def addBinary(a: str, b: str) -> str:
    
    if a == "0":
        return b
    if b == "0":
        return a

    sum = ""
    i = 0
    carry = 0
    
    # 1 1 0 1
    #   1 1 1

    diff = max(len(b), len(a)) - min(len(a), len(b))
    
    if len(b) < len(a):
        b = str("0" * diff) +  b
    elif len(a) < len(b):
        a = str("0" * diff) + a

    a = a[::-1]
    b = b[::-1]
    
    while i < len(a):
        # 1 + 1
        if int(a[i]) + int(b[i]) == 2:
            
            # with carry
            if carry == 1:
                sum += '1'     
            
            # without carry
            else:
                sum += '0'               
            # updating next carry
            carry = 1
        
        # 0 + 1
        if int(a[i]) + int(b[i]) == 1:
            if carry == 1:
                sum += '0'
                carry = 1
            else:
                sum += '1'
                carry = 0
        # 0 + 0
        if int(a[i]) + int(b[i]) == 0:
            if carry == 1:
                sum += '1'
            else:
                sum += '0'
            carry = 0
        i += 1
    # add remaining carry in the end
    if carry == 1:
        sum += '1'

    return sum[::-1]

