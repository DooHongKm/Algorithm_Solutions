from heapq import heapify, heappush, heappop

def solution(scovile, K):
    
    answer = 0
    
    heapify(scovile)
    while len(scovile) > 1:
        first = heappop(scovile)
        if first >= K:
            return answer
        second = heappop(scovile)
        heappush(scovile, first + second * 2)
        answer += 1
        
    if scovile[0] >= K:
        return answer
    return -1