def isValid(s: str) -> bool:
    stack = []
    top = 0
    for char in s:
        if char == "[" or char == "(" or char == "{":
            stack.append(char)
            top += 1
        elif (char == "}" and stack[top] == "{") or (char == "]" and stack[top] == "[") or (char == ")" and stack[top] == "("):
            stack.pop()
            top -= 1

    return True if top == 0 else False
if isValid("(((([[[{{}}]]]))))"):
    print("True")