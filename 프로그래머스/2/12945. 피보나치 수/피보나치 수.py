def solution(n):
    
    fibonacci = [0, 1]
    for _ in range(n - 1):
        temp = fibonacci[-2] + fibonacci[-1]
        fibonacci.append(temp)
    
    answer = fibonacci[-1] % 1234567

    return answer