import sys

n = int(sys.stdin.readline())
deque = []

def run(command):
  temp = command.split()
  if len(temp) == 2:
    left = temp[0]
    right = int(temp[1])
  else:
    left = temp[0]
  if left == "push_front":
    deque.insert(0, right)
  elif left == "push_back":
    deque.append(right)
  elif left == "pop_front":
    if len(deque) == 0: print(-1)
    else: print(deque.pop(0))
  elif left == "pop_back":
    if len(deque) == 0: print(-1)
    else: print(deque.pop(-1))    
  elif left == "size":
    print(len(deque))
  elif left == "empty":
    if len(deque) == 0: print(1)
    else: print(0)
  elif left == "front":
    if len(deque) == 0: print(-1)
    else: print(deque[0])
  elif left == "back":
    if len(deque) == 0: print(-1)
    else: print(deque[-1])
    
for _ in range(n):
  run(sys.stdin.readline().rstrip())