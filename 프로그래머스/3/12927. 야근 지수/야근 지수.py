def solution(n, works):
    
    result = 0
    
    rWork = 0
    rTime = 0
    sum_ = (sum(works) - n) // len(works)
    if sum_ < 0:
        return 0
    
    for i in range(sum_, max(works) + 1):
        count = 0
        for work in works:
            if work > i:
                count += work - i
        if n >= count:
            rWork = i
            rTime = n - count
            break
            
    works.sort(reverse=True)
    for work in works:
        temp = rWork
        if work < rWork:
            temp = work
        if temp > 0 and rTime > 0:
            result += (temp - 1) ** 2
            rTime -= 1
        else:
            result += temp ** 2
            
    return result
        
    