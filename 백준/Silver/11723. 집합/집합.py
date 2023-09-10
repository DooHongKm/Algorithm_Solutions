import sys
from collections import deque

n = int(sys.stdin.readline())
s = set()

for _ in range(n):
  command = list(sys.stdin.readline().split())
  if command[0] == "add":
    num = int(command[1])
    s.add(num)
  elif command[0] == "remove":
    num = int(command[1])
    s.discard(num)
  elif command[0] == "check":
    num = int(command[1])
    if num in s:
      print(1)
    else:
      print(0)
  elif command[0] == "toggle":
    num = int(command[1])
    if num in s:
      s.discard(num)
    else:
      s.add(num)
  elif command[0] == "all":
    s = set([i for i in range(1, 21)])
  elif command[0] == "empty":
    s.clear()