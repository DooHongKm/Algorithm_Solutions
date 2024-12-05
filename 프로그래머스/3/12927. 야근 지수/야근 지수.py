    # heapify(works := [-i for i in works])
    # for i in range(min(n, abs(sum(works)))):
    #     heappush(works, heappop(works)+1)
    # return sum([i*i for i in works])

from heapq import heapify, heappush, heappop

def solution(n, works):
    
    if sum(works) < n:
        return 0
    
    works = [-work for work in works]
    heapify(works)
    
    for i in range(n):
        heappush(works, heappop(works) + 1)
        
    result = 0
    for work in works:
        result += work ** 2
        
    return result