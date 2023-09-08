import sys

k = int(sys.stdin.readline())

stack = []
for _ in range(k):
  num = int(sys.stdin.readline())
  if num == 0:
    stack.pop()
  else:
    stack.append(num)

result = 0
for num in stack:
  result += num
print(result)