import sys

n, m, b = map(int, sys.stdin.readline().split())
shape = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

sum_ = 0
min_ = 256
for s in shape:
  sum_ += sum(s)
  min_ = min(min_, min(s))
max_ = (sum_ + b) // (n * m)

best_floor = 0
best_time = sys.maxsize
for i in range(min_, max_+1):
  temp1 = 0
  temp2 = 0
  for row in shape:
    for num in row:
      if num >= i:
        temp1 += (num - i) 
      else:
        temp2 += (i - num)
  if temp1 + b >= temp2:
    if temp1 * 2 + temp2 <= best_time:
      best_num = i
      best_time = temp1 * 2 + temp2
print(best_time, best_num)