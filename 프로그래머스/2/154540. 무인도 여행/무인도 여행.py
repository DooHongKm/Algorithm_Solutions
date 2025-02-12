def solution(maps):
    
    result = []
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    for j in range(len(maps)):
        for i in range(len(maps[0])):
            if maps[j][i] != "X" and not visited[j][i]:
                count = 0
                stack = []
                stack.append((i, j))
                while stack:
                    x, y = stack.pop()
                    if visited[y][x]:
                        continue
                    count += int(maps[y][x])
                    visited[y][x] = True
                    for n in range(4):
                        nx = x + dx[n]
                        ny = y + dy[n]
                        if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps) and maps[ny][nx] != "X":
                            stack.append((nx, ny))
                result.append(count)
            else:
                visited[j][i] = True
                
    if len(result) == 0:
        return [-1]
    return sorted(result)
                        
                    
            