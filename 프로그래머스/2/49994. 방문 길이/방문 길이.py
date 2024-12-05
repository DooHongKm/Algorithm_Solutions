def solution(dirs):
    
    direction = {"U":(0, 1), "D":(0, -1), "L":(-1, 0), "R":(1, 0)}
    
    visited = [(0, 0)]
    for d in dirs:
        dx, dy = direction[d]
        cx, cy = visited[-1]
        nx = cx + dx
        ny = cy + dy
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        visited.append((nx, ny))
        
    result = set()
    for i in range(len(visited) - 1):
        x, y = visited[i]
        nx, ny = visited[i + 1]
        result.add((x, y, nx, ny))
        result.add((nx, ny, x, y))
        
    return len(result) // 2
        
    