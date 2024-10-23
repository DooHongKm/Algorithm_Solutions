def solution(n):

    f = [0, 1]
        
    for i in range(n):
        f.append(f[i] + f[i + 1])
    
    
    

    return f[n] % 1234567