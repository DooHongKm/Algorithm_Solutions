def solution(n):

    result = 0
    
    while n > 0:
        if n % 2 == 1:
            n -= 1
            result += 1
        else:
            n //= 2
            
    return result
            
        