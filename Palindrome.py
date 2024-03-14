def isPalindrome(x: int) -> bool:
    # if list(str(x)) == list(str(x)[::-1]):
    #     return True
    # else:
    #     return False
    
    # or

    # return (True if list(str(x)) == list(str(x)[::-1]) else False)

    # or

    # if x<0:
    #     return False
    # elif str(x)==str(x)[::-1]:
    #     return True
    # else: 
    #     return False

    return str(x)==str(x)[::-1]


print("Yes") if isPalindrome(int(input())) else print("No")
