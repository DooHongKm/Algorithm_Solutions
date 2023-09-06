import sys

n = int(sys.stdin.readline())
my_cards = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

result = [0] * 20000001
for card in my_cards:
  result[card+10000000] += 1
for number in numbers:
  print(result[number+10000000], end=' ')