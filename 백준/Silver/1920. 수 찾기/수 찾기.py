import sys

n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
A.sort()

def b_search(list, num):
  l = 0
  r = n-1
  while l < r:
    mid = (l + r) // 2
    if list[mid] == num:
      return 1
    elif list[mid] > num:
      r = mid - 1
    else:
      l = mid + 1
  if list[l] == num:
    return 1
  else:
    return 0

for num in numbers:
  print(b_search(A, num))