def solution(progresses, speeds):
    
    answer = []
    temp = []
    
    for i in range(len(progresses)):
        p = progresses[i]
        s = speeds[i]
        time = (100 - p) // s
        if (100 - p) % s > 0:
            time += 1
        temp.append(time)

    while len(temp) > 0:
        count = 1
        t = temp.pop(0)
        while len(temp) > 0 and t >= temp[0]:
            count += 1
            temp.pop(0)
        answer.append(count)
            
    return answer
        
        
        