from collections import Counter

def solution(topping):
    
    answer = 0
    
    a = Counter(topping)
    b = {}
    
    for t in topping:
        a[t] -= 1
        b[t] = 1
        if a[t] == 0:
            a.pop(t)
        if len(a) == len(b):
            answer += 1
            
    return answer