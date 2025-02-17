from collections import deque

def solution(n, edge):
    
    # 1번 노드로부터 각 노드까지의 거리
    result = [0 for _ in range(n + 1)]
    
    # edge의 딕셔너리화
    dic = {}
    for a, b in edge:
        if a in dic:
            dic[a].append(b)
        else:
            dic[a] = [b]
        if b in dic:
            dic[b].append(a)
        else:
            dic[b] = [a]
    
    # 탐색할 노드 큐
    queue = deque([1])
    while queue:
        cur = queue.popleft()
        for c in dic[cur]:
            if c != 1 and result[c] == 0:
                queue.append(c)
                result[c] = result[cur] + 1
                
    # 최대 거리를 구해서 그 개수를 반환
    return result.count(max(result[1:]))