def solution(m, n, board):

    answer = 0
    
    board.reverse()
    board = [[row[i] for row in board] for i in range(n)]

    while True:
        matched = {}
        for y in range(n - 1):
            length = min(len(board[y]), len(board[y + 1]))
            for x in range(length - 1):
                cur = board[y][x]
                if cur == board[y][x + 1] and cur == board[y + 1][x] and cur == board[y + 1][x + 1]:
                    if y in matched:
                        matched[y].update([x, x + 1])
                    else:
                        matched[y] = set([x, x + 1])
                    if y + 1 in matched:
                        matched[y + 1].update([x, x + 1])
                    else:
                        matched[y + 1] = set([x, x + 1])
        for y, x in matched.items():
            temp = sorted(x, reverse=True)
            for t in temp:
                del board[y][t]
                answer += 1
        if len(matched) == 0:
            break
            
    return answer