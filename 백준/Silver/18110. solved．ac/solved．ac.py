import sys

n = int(sys.stdin.readline())

if n == 0:
  print(0)

else:
  sum = 0
  difficulties = [0] * n
  for i in range(n):
    difficulties[i] = int(sys.stdin.readline())
  difficulties.sort()
  exception = int(n * 0.15 + 0.5)
  for i in range(exception, n - exception):
    sum += difficulties[i]
  average = int(sum / (n - (2 * exception)) + 0.5)
  print(average)