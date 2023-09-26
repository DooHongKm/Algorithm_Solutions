import heapq

def solution(scovile, K):
    h = []
    answer = 0
    for s in scovile:
        heapq.heappush(h, s)
    while h[0] < K:
        heapq.heappush(h, heapq.heappop(h) + heapq.heappop(h) * 2)
        answer += 1
        if len(h) == 1 and h[0] < K:
            return -1
    return answer