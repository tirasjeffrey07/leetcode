""" 

count number of sub strings that start and end with 1

"""
def countSubstrings(s):
    # 100101
    # s    e 
    start, end = 0, len(s) - 1
    firstOne = 0 
    while True:

        # fix pointer at the last 
        if s[end] != "1":
            end -= 1
            
        # count number of first ones ie ones before the last one
        if s[start] == "1":
            firstOne += 1
        start += 1
        
        #
        if start ==  end:
            break

    return firstOne + (firstOne - 1)

"""
Use the above two pointer approach or 
use the following formula:
1) compute the number of ones in the entire string
2) apply it here:
   ( count * (count - 1) ) // 2 


"""