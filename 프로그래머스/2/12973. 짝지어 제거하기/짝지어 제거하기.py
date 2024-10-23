def solution(s):
    
    stack = [s[0]]
    s = s[1:]
    for a in s:
        if len(stack) > 0:
            if a == stack[-1]:
                stack.pop()
            else:
                stack.append(a)
        else:
            stack.append(a)
            
    if len(stack) == 0:
        return 1
    return 0
                