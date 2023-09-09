import sys

k, n = map(int, sys.stdin.readline().split())
lines = [int(sys.stdin.readline()) for _ in range(k)]

short = 1
long = max(lines)
while long >= short:
  mid = (short + long) // 2
  temp = 0
  for line in lines:
    temp += (line // mid)
  if temp < n:
    long = mid - 1
  else:
    short = mid + 1
print(long)