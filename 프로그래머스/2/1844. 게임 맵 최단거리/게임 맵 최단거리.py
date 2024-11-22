from collections import deque

def solution(maps):
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    
    queue = deque([(1, 0, 0)])
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = 1
    
    while queue:
        idx, x, y = queue.popleft()
        if y == len(maps) - 1 and x == len(maps[0]) - 1:
            return idx
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] == 1 and visited[ny][nx] == 0:
                queue.append((idx+1, nx, ny))
                visited[ny][nx] = 1
                
    return -1