import sys

n, m, b = map(int, sys.stdin.readline().split())
shape = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

best_floor = 0
best_time = sys.maxsize
for i in range(257):
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