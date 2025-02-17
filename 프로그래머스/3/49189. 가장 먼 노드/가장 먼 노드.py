from collections import deque

def solution(n, edge):
    edge = sorted(edge)  # [[1, 2], [1, 3], [2, 4], [3, 2], [3, 6], [4, 3], [5, 2]]
    distance = [0] * (n+1) # 각 노드별로 노드 1부터의 거리
    queue = deque()
    graph = [[] for _ in range(n+1)]
    answer = 0

    for i in edge:  # 인접 리스트 방식으로 그래프 구현
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    queue.append(1)  # 큐에 첫 번째로 방문할 노드 번호를 추가
    distance[1]=1  # 방문한 노드의 거리를 1로 설정

    while queue:
        current = queue.popleft()
        for node in graph[current]:
            if distance[node] == 0:  # 방문 여부를 확인하고, 방문한 적이 없는 경우
                queue.append(node)  # 노드를 큐에 추가
                distance[node] = distance[current] + 1  # 해당 노드의 값을 현재 노드의 값에 1을 더한 값으로 변경

    max_distance = max(distance)  # distance에서 최댓값을 찾은 후 해당 값과 동일한 요소의 개수만큼 answer에 더한다.
    for j in distance:
        if j == max_distance:
            answer += 1
    return answer