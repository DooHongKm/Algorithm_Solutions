from collections import deque

def solution(maps):
    
    height = len(maps)
    width = len(maps[0])
    visited = [[False] * width for _ in range(height)]
    
    q = deque()
    q.append((0, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[0][0] = True
    
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < width and 0 <= ny < height and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    print(ny, nx)
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    maps[ny][nx] = maps[y][x] + 1
                    print(maps[ny][nx])
    if maps[height-1][width-1] == 1:
        return -1
    else:
        return maps[height-1][width-1]