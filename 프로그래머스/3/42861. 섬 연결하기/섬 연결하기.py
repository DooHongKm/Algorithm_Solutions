import heapq as hq

def solution(n, costs):

    result = 0
    
    checked = [False for _ in range(n)]
    table = [[0 if i == j else float('inf') for i in range(n)] for j in range(n)]
    
    for cost in costs:
        a, b, c = cost
        table[a][b] = c
        table[b][a] = c
        
    heap = [(0, 0)]
    while heap:
        cost, idx = hq.heappop(heap)
        if checked[idx]:
            continue
        else:
            checked[idx] = True
        result += cost
        for i in range(n):
            if i != idx and table[idx][i] != float('inf'):
                hq.heappush(heap, (table[idx][i], i))
        
    return result
    
        
        