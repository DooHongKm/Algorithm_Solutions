def check(s):
    stack = []
    for p in s:
        if len(stack) == 0:
            stack.append(p)
        else:
            if stack[-1] == "(" and p == ")":
                stack.pop()
                continue
            elif stack[-1] == "{" and p == "}":
                stack.pop()
                continue
            elif stack[-1] == "[" and p == "]":
                stack.pop()
                continue
            else:
                stack.append(p)
    if len(stack) == 0:
        return 1
    return 0



def solution(s):
    
    result = 0
    
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        result += check(temp)
    
    return result