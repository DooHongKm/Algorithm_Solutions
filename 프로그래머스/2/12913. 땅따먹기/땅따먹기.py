def solution(land):

    scores = [land[0][i] for i in range(4)]
    
    for i in range(1, len(land)):
        nscores = [0] * 4
        for j in range(4):
            temp = scores[:j] + scores[j+1:]
            nscores[j] = max(temp) + land[i][j]
        scores = nscores
        
    return max(scores)