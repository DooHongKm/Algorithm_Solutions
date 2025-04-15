from collections import deque

def solution(n, roads, sources, destination):
    
    result = [0 if i == destination else -1 for i in range(n + 1)]
    checked = [1 if i == destination else 0 for i in range(n + 1)]
    
    table = [[] for _ in range(n + 1)]
    for a, b in roads:
        table[a].append(b)
        table[b].append(a)
        
    q = deque([(destination, 0)])
    while q:
        cur, count = q.popleft()
        for i in table[cur]:        
            if checked[i] == 1:
                continue
            if table[cur] :
                q.append((i, count + 1))
                result[i] = count + 1
                checked[i] = 1
        
    return [result[source] for source in sources]