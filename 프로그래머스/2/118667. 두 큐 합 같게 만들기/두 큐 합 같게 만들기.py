from collections import deque

def solution(queue1, queue2):

    q1 = deque(queue1)
    q2 = deque(queue2)
    
    sum_ = sum(queue1 + queue2)
    if sum_ % 2 == 1:
        return -1
    
    target = sum_ // 2
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    for i in range(300000):
        if sum1 == sum2:
            return i
        if sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            sum1 += num
            sum2 -= num
        
    return -1
            
    
    