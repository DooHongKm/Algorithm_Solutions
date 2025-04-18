def solution(k, d):

    answer = 0
    maximumY = k * (d // k)
    
    for x in range(0, d + 1, k):
        curveY = (d ** 2 - x ** 2) ** 0.5
        answer += curveY // k + 1
        
    return answer