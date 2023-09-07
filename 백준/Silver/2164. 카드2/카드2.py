import sys
from collections import deque

n = int(sys.stdin.readline())
cards = deque([i + 1 for i in range(n)])
while len(cards) > 1:
  cards.popleft()
  cards.append(cards.popleft())
print(cards[0])