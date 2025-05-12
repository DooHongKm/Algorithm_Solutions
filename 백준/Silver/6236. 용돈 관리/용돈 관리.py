import sys

result = 0

N, M = map(int, sys.stdin.readline().rstrip().split())
costs = [int(sys.stdin.readline().rstrip()) for _ in range(N)]

left = max(costs)
right = sum(costs)
    
while left <= right:
    mid = (left + right) // 2
        
    cur = mid
    count = 1
    for cost in costs:
        if cost > cur:
            cur = mid
            count += 1
        cur -= cost
        
    if count > M:
        left = mid + 1
    else:
        result = mid
        right = mid - 1
    
print(result)