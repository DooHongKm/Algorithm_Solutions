T = int(input())
for count in range(1, T + 1):

    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    
    board = [input().split() for _ in range(4)]

    numbers = []

    def dfs(x, y, t):
        if len(t) == 7:
            numbers.append(t)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 4:
                dfs(nx, ny, t + board[ny][nx])

    for i in range(4):
        for j in range(4):
            dfs(j, i, board[i][j])	
    numbers = set(numbers)

    print(f"#{count} {len(numbers)}")
