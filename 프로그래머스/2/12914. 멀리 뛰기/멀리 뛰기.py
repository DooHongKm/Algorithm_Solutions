# count(n) = count(n-1) + count(n-2)

def solution(n):
    
    temp1 = 1
    temp2 = 2
    for i in range(3, n+1):
        temp3 = temp1 + temp2
        temp1 = temp2
        temp2 = temp3
        
    if n < 3: return n
    return temp2 % 1234567
        

    