def solution(money):
    
    money = [money[1:], money[:-1]]
    
    result = 0
    for m in money:
        dp = [0 for _ in range(len(m))]
        dp[0] = m[0]
        dp[1] = max(m[0], m[1])
        for i in range(2, len(m)):
            dp[i] = max(dp[i - 1], dp[i - 2] + m[i])
        result = max(result, dp[-1])
        
    return result
    