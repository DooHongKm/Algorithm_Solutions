import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

result = 0
A.sort()
        
for i in range(N):
    a = A[i]
    left = 0
    right = N - 1
    
    while left < right:
        if left == i:
            left += 1
            continue
        if right == i:
            right -= 1
            continue
        
        sum_ = A[left] + A[right]
        if sum_ == a:
            result += 1
            break
        elif sum_ > a:
            right -= 1
        else:
            left += 1
        
print(result)