from collections import deque

def solution(x, y, n):
    
    queue = deque([(x, 0)])
    visited = set()
    
    if x == y:
        return 0
    
    while queue:
        num, idx = queue.popleft()
        numbers = [num+n, num*2, num*3]
        for number in numbers:
            if number < y and number not in visited:
                queue.append((number, idx+1))
                visited.add(number)
            elif number == y:
                return idx + 1
        
    return -1