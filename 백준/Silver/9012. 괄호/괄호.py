import sys

n = int(sys.stdin.readline())
for _ in range(n):
  count = 0
  vps = True
  temp = sys.stdin.readline().rstrip()
  for chr in temp:
    if chr == '(': count += 1
    else: count -= 1
    if count == -1:
      vps = False
      break
  if count != 0: vps = False
  if vps == True:
    print("YES")
  else:
    print("NO")