from collections import deque

def solution(N, road, K):

    results = [float("inf") for _ in range(N + 1)]
    results[1] = 0
    
    roads = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for r in road:
        start, end, distance = r
        if roads[start][end] == 0:
            roads[start][end] = distance
            roads[end][start] = distance
        else:
            roads[start][end] = min(roads[start][end], distance)
            roads[end][start] = min(roads[end][start], distance)
    
    q = deque([1])
    while q:
        idx = q.popleft()
        for i in range(N + 1):
            temp = roads[idx][i]
            if temp != 0 and results[idx] + temp < results[i]:
                q.append(i)
                results[i] = results[idx] + temp
    
    answer = 0
    for res in results:
        if K >= res:
              answer += 1
    
    return answer
    
            