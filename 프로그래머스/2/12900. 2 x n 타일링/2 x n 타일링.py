# 1과 2를 조합하여 n을 만들기

def solution(n):

    if n == 1 or n == 2:
        return n
    
    temp = [0 for _ in range(n + 1)]
    temp[1] = 1
    temp[2] = 2
    
    for i in range(3, n + 1):
        temp[i] = (temp[i - 1] + temp[i - 2]) % 1000000007
        
    return temp[n]
    
    