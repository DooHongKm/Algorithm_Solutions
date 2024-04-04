def solution(want, number, discount):
    
    answer = 0
    
    table = [[0 for _ in range(len(discount) + 1)] for _ in range(len(want))]
    for i in range(len(discount)):
        for j in range(len(want)):
            if discount[i] == want[j]:
                for k in range(max(1, i - 8), i + 2):
                    table[j][k] += 1
                break
    
    for i in range(1, len(table[0])):
        for j in range(len(want)):
            if table[j][i] != number[j]:
                break
            if j == len(want) - 1:
                answer += 1
                break
    
    return answer