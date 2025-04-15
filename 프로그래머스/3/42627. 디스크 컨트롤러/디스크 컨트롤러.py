def solution(jobs):
    
    cur = 0
    sum_ = 0
    l = len(jobs)
    
    jobs = sorted([[jobs[i][1], jobs[i][0], i] for i in range(l)])
    
    while jobs:
        exist = False
        for i in range(len(jobs)):
            if jobs[i][1] <= cur:
                exist = True
                cur += jobs[i][0]
                sum_ += (cur - jobs[i][1])
                del jobs[i]
                break
        if not exist:
            cur += 1
            
    return sum_ // l