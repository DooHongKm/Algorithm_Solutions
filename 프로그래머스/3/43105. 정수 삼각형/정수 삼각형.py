def solution(triangle):

    l = len(triangle)
    dp = [[0] * i for i in range(1, l+1)]
    dp[0][0] = triangle[0][0]
    
    for i in range(l - 1):
        for j in range(i + 1):
            temp = dp[i][j]
            dp[i+1][j] = max(dp[i+1][j], temp+triangle[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], temp+triangle[i+1][j+1])
            
    return max(dp[-1])

        
            