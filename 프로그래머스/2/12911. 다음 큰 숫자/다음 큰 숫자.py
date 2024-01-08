def solution(n):
    
    answer = 0
    
    count_n = 0
    binary_n = bin(n)[2:]
    for num in binary_n:
        if num == '1':
            count_n += 1
    
    for i in range(n + 1, 1000001):
        count_i = 0
        binary_i = bin(i)[2:]
        for num in binary_i:
            if num == '1':
                count_i += 1
        if count_i == count_n:
            answer = i
            break

    return answer