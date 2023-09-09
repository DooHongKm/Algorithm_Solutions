import sys
from collections import deque

n = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(n)]
point = 0
number = 1

stack = []
result = []
while True:
  if len(stack) == 0:
    if number == n + 1:
      for res in result:
        print(res)
      break
    else:
      stack.append(number)
      result.append("+")
      number += 1
    continue
  else:
    if stack[-1] == numbers[point]:
      stack.pop()
      result.append("-")
      point += 1
    else:
      stack.append(number)
      result.append("+")
      number += 1
  if number > n + 1:
    print("NO")
    break