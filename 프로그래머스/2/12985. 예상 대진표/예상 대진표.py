def solution(n,a,b):

    answer = 1
    if (a + 1) // 2 == (b + 1) // 2:
        return answer
    
    while True:
        answer += 1
        a = (a + 1) // 2
        b = (b + 1) // 2
        if (a + 1) // 2 == (b + 1) // 2:
            return answer
        
        