from collections import Counter


def solution(topping):
    
    answer = 0
    
    big = Counter(topping)
    small = set()
    for t in topping:
        big[t] -= 1
        if big[t] == 0:
            big.pop(t)
        small.add(t)
        if len(big) == len(small):
            answer += 1

    return answer