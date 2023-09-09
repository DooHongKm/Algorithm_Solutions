import sys
from collections import deque

a = int(sys.stdin.readline())
for _ in range(a):
  n, m = map(int, sys.stdin.readline().split())
  scores = deque(list(map(int, sys.stdin.readline().split())))
  count = 0
  while True:
    max_ = max(scores)
    top = scores.popleft()
    if top == max_:
      count += 1
      if m == 0:
        print(count)
        break
      else:
        m -= 1
    else:
      scores.append(top)
      if m == 0:
        m = len(scores) - 1
      else:
        m -= 1