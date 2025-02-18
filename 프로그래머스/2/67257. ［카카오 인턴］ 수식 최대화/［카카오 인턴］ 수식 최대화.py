from itertools import permutations

def solution(expression):
    
    answer = 0
    
    perm = list(permutations(["+", "-", "*"]))
    for first, second, third in perm:
        temp = expression.split(third)
        temp = [t.split(second) for t in temp]
        for i in range(len(temp)):
            for j in range(len(temp[i])):
                temp[i][j] = str(eval(temp[i][j]))
            temp[i] = str(eval(second.join(temp[i])))
        result = eval(third.join(temp))
        answer = max([result, -result, answer])
        
    return answer