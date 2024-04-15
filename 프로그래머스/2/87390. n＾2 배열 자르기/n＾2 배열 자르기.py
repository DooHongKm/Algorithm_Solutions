def solution(n, left, right):
    
    result = []
    l1 = left // n
    l2 = left % n
    r1 = right // n
    count = right - left + 1
    
    for i in range(l1, r1 + 1):
        temp = [t + 1 for t in range(n)]
        for j in range(i):
            temp[j] = i + 1
        result += temp
    
    result = result[l2:l2+count]
    
    return result