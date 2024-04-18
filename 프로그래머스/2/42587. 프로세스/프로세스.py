from collections import deque

def solution(priorities, location):

    stack = []
    a = deque([i for i in range(len(priorities))])
    p = deque(priorities)
    l = location
    
    while p:
        temp = p.popleft()
        temp2 = a.popleft()
        if not p:
            stack.append(temp2)
            break
        for i, n in enumerate(p):
            if temp >= n and i == len(p) - 1:
                stack.append(temp2)
                break
            elif temp >= n:
                continue
            else:
                p.append(temp)
                a.append(temp2)
                break
                
    result = stack.index(l) + 1
    
    return result