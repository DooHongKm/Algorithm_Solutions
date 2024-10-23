def solution(n):

    count = 0
    
    for i in range(1, n + 1):
        temp = i
        if temp == n:
            count += 1
            break
        for j in range(i + 1, n + 1):
            if temp == n:
                count += 1
                break
            elif temp > n:
                break
            else:
                temp += j
                
    return count
                