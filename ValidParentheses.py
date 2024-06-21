
def isValid( s: str) -> bool:
    if len(s) % 2 != 0:
        return False
    stack = []
    for char in s:
        if char == "(" or char == "{" or char == "[":
            stack.append(char)

        elif stack:
            if char == ")" and stack[-1] == "(":
                stack.pop()
            
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        else:
            return False
            

    if stack:
        return False
    return True