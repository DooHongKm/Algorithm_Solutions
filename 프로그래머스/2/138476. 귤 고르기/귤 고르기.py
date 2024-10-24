def solution(k, tangerine):
    
    temp = [0 for _ in range(10000001)]
    
    for t in tangerine:
        temp[t] += 1
        
    temp.sort(reverse=True)
    
    count = 1
    
    for t in temp:
        if t >= k:
            break
        else:
            k -= t
            count += 1
    
    return count
        
