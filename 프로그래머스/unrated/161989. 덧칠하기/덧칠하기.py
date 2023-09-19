def solution(n, m, section):
    start = section[0]
    finish = section[-1]
    temp = start - 1
    count = 0
    for sec in section:
        if sec > temp:
            count += 1
            temp = sec + m - 1
        else:
            continue
        if temp >= finish:
            break
    return count