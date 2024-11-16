T = int(input())
for count in range(1, T + 1):

    board = [list(map(int, input().split())) for _ in range(4)]

    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    numbers = []

    def dfs(x, y, t):
        if len(t) == 7:
            if t not in numbers:
                numbers.append(t)
            return
        if x > 0:
            dfs(x - 1, y, t + str(board[y][x - 1]))
        if x < 3:
            dfs(x + 1, y, t + str(board[y][x + 1]))
        if y > 0:
            dfs(x, y - 1, t + str(board[y - 1][x]))
        if y < 3:
            dfs(x, y + 1, t + str(board[y + 1][x]))

    for i in range(4):
        for j in range(4):
            dfs(j, i, str(board[i][j]))

    print(f"#{count} {len(numbers)}")
