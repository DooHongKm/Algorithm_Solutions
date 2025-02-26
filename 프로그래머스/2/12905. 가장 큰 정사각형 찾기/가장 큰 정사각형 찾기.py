def solution(board):
    height = len(board)
    width = len(board[0])
    
    dp = board.copy()
    for j in range(1, height):
        for i in range(1, width):
            if dp[j][i] == 1:
                dp[j][i] = min(board[j - 1][i - 1], board[j - 1][i], board[j][i - 1]) + 1
    
    result = 0
    for j in range(height):
        result = max(result, max(dp[j]))
        
    return result ** 2