import sys

n = int(sys.stdin.readline())

result = -1
for i in range(n // 5 + 1):
  big = n // 5 - i
  if (n - (big * 5)) % 3 == 0:
    small = (n - (big * 5)) // 3
    result = big + small
    break

print(result)