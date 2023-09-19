def solution(t, p):
    count = 0
    num = int(p)
    for i in range(len(t) - len(p) + 1):
        temp = int(t[i:i+len(p)])
        if temp <= num:
            count += 1
    return count