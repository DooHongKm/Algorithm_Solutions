def solution(sticker):

    if len(sticker) == 1:
        return sticker[0]
    if len(sticker) == 2:
        return max(sticker[0], sticker[1])
    
    stickers = [sticker[1:], sticker[:-1]]
    
    result = 0
    for s in stickers:
        dp = [0 for _ in range(len(s))]
        dp[0] = s[0]
        dp[1] = max(s[0], s[1])
        for i in range(2, len(s)):
            dp[i] = max(dp[i - 1], dp[i -2] + s[i])
        result = max(result, dp[-1])
        
    return result
    
        