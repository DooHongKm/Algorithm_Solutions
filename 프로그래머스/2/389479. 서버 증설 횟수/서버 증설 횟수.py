def solution(players, m, k):
    result = 0
    length = len(players)
    
    for i, player in enumerate(players):
        add = player // m
        if add > 0:
            result += add
            for j in range(i + 1, min(length, i + k)):
                players[j] -= add * m
        
    return result