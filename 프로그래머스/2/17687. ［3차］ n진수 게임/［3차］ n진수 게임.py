def solution(n, t, m, p):

    limit = m * (t - 1) + p
    
    idx = 0
    answer = []
    while len(answer) < limit:
        temp = idx
        numbers = []
        while temp >= n:
            numbers.append(temp % n)
            temp = temp // n
        numbers.append(temp)
        numbers.reverse()
        answer += numbers
        idx += 1
    
    result = ""
    for i in range(t):
        temp = answer[i * m + p - 1]
        if temp > 9:
            result += chr(temp + 55)
        else:
            result += str(temp)
    
    return result            
            