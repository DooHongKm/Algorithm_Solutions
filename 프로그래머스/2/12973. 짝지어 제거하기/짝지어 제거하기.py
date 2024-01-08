def solution(s):
    
    stack = []
    s = list(s)
    stack.append(s.pop())
    
    while True:
        if len(s) == 0:
            break
        temp = s.pop()
        if len(stack) == 0:
            stack.append(temp)
        elif stack[-1] == temp:
            stack.pop()
        else:
            stack.append(temp)
    
    if len(stack) == 0:
        return 1
    else:
        return 0