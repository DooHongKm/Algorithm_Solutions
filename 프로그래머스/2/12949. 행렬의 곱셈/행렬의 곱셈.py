def solution(arr1, arr2):
    
    sero = len(arr1)
    garo = len(arr2[0])
    cross = len(arr2)
    
    answer = [[0 for _ in range(garo)] for _ in range(sero)]
    
    for a in range(sero):
        for b in range(garo):
            for i in range(cross):
                answer[a][b] += arr1[a][i] * arr2[i][b]

    return answer
    
    
    
    
    
    
    
    return answer