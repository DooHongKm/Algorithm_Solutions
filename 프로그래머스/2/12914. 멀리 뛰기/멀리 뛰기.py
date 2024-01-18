def solution(n):
    
    if n == 1:
        return 1
    elif n == 2 :
        return 2
    
    stack = [0 for _ in range(n + 1)]
    stack[1] = 1
    stack[2] = 2
    for i in range(3, n + 1):
        stack[i] = stack[i - 2] + stack[i - 1]
        
    answer = stack[n] % 1234567  
    
    return answer