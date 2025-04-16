def solution(n, t, m, timetable):

    table = []
    for time in timetable:
        hour, minute = map(int, time.split(":"))
        table.append(hour * 60 + minute)
    table.sort()
        
    cTime = 540
    cTable = table.copy()
    while n > 1:
        for _ in range(m):
            if cTable[0] <= cTime:
                del cTable[0]
            else:
                break
        n -= 1
        cTime += t
        
    result = cTime
    if len(cTable) >= m:
        if cTable[m - 1] <= cTime:
            result = cTable[m - 1] - 1
        

    h = result // 60
    m = result % 60
    string_h = str(h) if h >= 10 else "0" + str(h)
    string_m = str(m) if m >= 10 else "0" + str(m)
    
    return string_h + ":" + string_m