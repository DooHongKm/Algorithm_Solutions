import sys

n = int(sys.stdin.readline())
stack = []

def run(command):
  temp = command.split()
  if len(temp) == 2:
    left = temp[0]
    right = int(temp[1])
  else:
    left = temp[0]
  if left == "push":
    stack.append(right)
  elif left == "pop":
    if len(stack) == 0: print(-1)
    else: print(stack.pop(-1))
  elif left == "size":
    print(len(stack))
  elif left == "empty":
    if len(stack) == 0: print(1)
    else: print(0)
  elif left == "top":
    if len(stack) == 0: print(-1)   
    else: print(stack[-1])
    
for _ in range(n):
  run(sys.stdin.readline().rstrip())